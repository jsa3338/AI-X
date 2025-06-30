import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def askGpt(prompt):
    "매개변수로 받은 prompt를 3줄로 요약"
    load_dotenv()
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages = [
            {'role':'system', 'content':'You are a special assistant of briefing in Korean text. use bullets and in korea'},
            {'role':'user', 'content':prompt}
        ]
    )
    return response.choices[0].message.content

# 기능구현
def main():
    st.header("요약 프로그램")
    st.markdown("---")
    text = st.text_area("요약할 글을 입력하세요")
    if st.button("요약하기"):
        prompt = f'summarize in 1 line. text:{text}'
        result = askGpt(prompt=prompt)
        st.info(result)



if __name__=="__main__":
    main()