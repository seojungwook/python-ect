import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import certifi

def down_img(url):
    name = int(round(time.time()*1000))
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

def spider(max_page):

    url =input("크롤링할 페이지의 URL을 입력하세요:")
    YN = input("해당사이트의 이미지을 다운받고 싶으시면 Y 를 눌러주세요:")
    page =1
    while page < max_page:


        source_code = requests.get(url, verify=certifi.where())
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')
        #print(soup)

        cou = 1
        for img in soup.select("img"):
            v = img.get('src')
            ex = img.get('data-src')
            print(v)
            if(YN == "Y"):
                down_img(v)
            if(ex != None):
                print(ex)
                if (YN == "Y"):
                    down_img(ex)
            print("<-----잘라------------------------------>",cou)
            
            #삽질의 흔적 ㅠㅠ 2017.11.22 jw
            #start=int(str(v).find('src="'))+5
            #end = int(str(v).find())
            #print(str(v)[start:end])
            #if(str(v)[start:end] != ""):
                #down_img(str(v)[start:end])
            #흐느적흐느적 ㅠㅠ

            cou+=1


        page+=1

spider(2)
