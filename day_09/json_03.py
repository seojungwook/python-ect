# -*- coding: utf-8 -*-

import json
import urllib.request

# 애플리케이션 등록시 발급 받은 값 입력
client_id = "mRSyMGsj_bLkhPLyQQU2" 
# 애플리케이션 등록시 발급 받은 값 입력
client_secret = "Za0qqgyKM7" 

url = "https://openapi.naver.com/v1/search/news.json"
# URL 내부에 한글데이터를 추가하기 위한 방법
encText = urllib.parse.quote("폭설")
query = f"?query={encText}&display=5"

request = urllib.request.Request(url + query)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    # response_body = response.read()
    # print(response_body.decode('utf-8'))
    
    json_data = json.load(response)
    for news in json_data["items"] :
        print(news["title"])
else:
    print("Error Code:" + rescode)















