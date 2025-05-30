# 카카오 번역기를 이용해 번역하기
# ch14_맞춤법후.txt 파일을 ch14_자동화영어번역본.txt 로 저장한다

# ch14_맞춤법후.txt 를 1000자로 쪼개기
with open('data/ch14_맞춤법후.txt', 'r', encoding='utf-8') as f:
    text = f.read()
ready_lists= []
while(len(text)>1000):
    temp = text[:1000]
    flag = temp.rfind('\n')
    temp = temp[:flag]
    ready_lists.append(temp)
    text = text[flag:]
ready_lists.append(text)

# 카카온 번역에서 번역 후 ch14_자동화영어번역본.txt 로 저장
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://translate.kakao.com')
time.sleep(0.5)
textarea = driver.find_element(By.ID, 'textareaWrite')
result = ''
for ready in ready_lists:
    time.sleep(0.5)
    textarea.send_keys(Keys.CONTROL, 'a')
    textarea.send_keys(ready)
    btn_trans = driver.find_element(By.CLASS_NAME, 'btn_translate')
    btn_trans.click()
    time.sleep(0.5)
    result_area = driver.find_element(By.CSS_SELECTOR, 'div.result_area').text    
    result += result_area +'\n\n'
#driver.close()

#번역한 결과 파일 출력
with open('data/ch14_자동화영어번역본.txt', 'w', encoding='utf-8') as f:
    f.write(result)
print('번역 완료')
