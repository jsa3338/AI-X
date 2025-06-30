# 자동완성이 안될 경우, 가상환경 설정이 안되어 있는 것이다 : ctrl_shift+p
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import os
import time
import warnings
warnings.filterwarnings("ignore", category= DeprecationWarning)

# 1. client 생성
load_dotenv('.env')
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# 2. assistant 생성
assistant_cs = client.beta.assistants.create(
    name='CustomerSupportBot',
    instructions='당신은 고객 지원 챗봇입니다. 사용자 문의에 대해 30자 이내로 친절한 답변을 하세요',
    model='gpt-4o-mini'
)
# 3. thread 생성
thread_cs = client.beta.threads.create()
print('챗봇이 시작됩니다. 종료를 원하시면 "종료"나 "exit"를 입력하세요')

while True:
    user_input = input('User : ').strip()
    if user_input.lower() in ('종료', 'exit'):
        print('챗봇이 종료됩니다. 이용해주셔서 감사합니다.')
        break
    if user_input == "":
        continue
    # 4~6 : user_input을 thread_cs에 추가하고 실행한 후 thread_cs에 입력된 최종 답변 출력
    # 4. 스레드에 인풋을 추가
    client.beta.threads.messages.create(
        thread_id=thread_cs.id,
        role='user',
        content=user_input
    )
    # 5. run
    client.beta.threads.runs.create_and_poll(
        thread_id=thread_cs.id,
        assistant_id=assistant_cs.id
    )
    # 6. 최종 답변 출력
    messages = client.beta.threads.messages.list(thread_id=thread_cs.id)
    assistant_reply = messages.data[0]
    reply_text = assistant_reply.content[0].text.value
    # print(f'user : {user_input}')
    print(f'assistant : {reply_text}')

# 7. 대화 이력 뽑아, 파일 출력
sorted_messages = sorted(messages.data,
                        key=lambda data : data.created_at)
with open('data/ch7_chat_history.txt', 'w', encoding='utf-8') as f:
    for message in sorted_messages:
        # datetime으로 변환 '생성시각 : ', message.created_at
        datetime_info = time.localtime(message.created_at)
        # 보기 좋은 문자열 형식으로 변환
        output_str = time.strftime("%Y-%m-%d %H:%M:%S", datetime_info)
        # 파일 출력
        f.write("{:9}({}) : {}\n".format(message.role, 
                                        output_str, 
                                        message.content[0].text.value) )
        
    