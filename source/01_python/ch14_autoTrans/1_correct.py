# 네이버 맞춤법 검사
# data/ch14_맞춤법전.txt 의 텍스트 내용을 가져와 교정하여 data/ch14_맞춤법후.txt 로 저장한다
from bs4 import BeautifulSoup
# ch14_맞춤법전.txt 를 300자로 쪼개기
with open('data/ch14_맞춤법전.txt', 'r', encoding='utf-8') as f:
    text = f.read()
ready_list=[]
while(len(text) >300):
    temp = text[:300]
    new_line_char_index = temp.rfind('\n')
    print(new_line_char_index)
    ready_list.append(text[:new_line_char_index])
    text = text[new_line_char_index:]
ready_list.append(text)

# 네이버 맞춤법 검사기 -> 검사 및 크롤링 -> 파일 작성
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://www.naver.com/')
input_el = driver.find_element(By.NAME, 'query')
input_el.send_keys('맞춤법 검사기')
input_el.send_keys(Keys.ENTER)
time.sleep(1)
results = ''
for ready in ready_list:
    textarea = driver.find_element(By.CLASS_NAME, 'txt_gray')
    textarea.send_keys(ready)
    button_chk = driver.find_element(By.CLASS_NAME, 'btn_check')
    button_chk.click()
    time.sleep(1)
    
    soup =  BeautifulSoup(driver.page_source, 'html.parser')
    result = soup.select_one('p._result_text.stand_txt').text
    results += result + '\n'
    button_del = driver.find_element(By.CLASS_NAME, 'delete_btn')
    button_del.click()
    time.sleep(0.5)
# driver.close()

# 파일 저장
with open('data/ch14_맞춤법후.txt', 'w', encoding='utf-8') as f:
    f.write(results)