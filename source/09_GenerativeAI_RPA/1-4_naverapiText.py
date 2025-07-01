# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv('Client_ID')
client_secret = os.getenv('Client_Secret')
print(client_id)
print(client_secret)
encText = urllib.parse.quote("포켄스")
media='shop'  # news
url = f"https://openapi.naver.com/v1/search/{media}?display=2&sort=date&query="+encText
# print(url)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)