# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
# urllib.request는 URL 정보를 활용하여 
# 요청을 실행할 수 있는 모듈
import urllib.request as req

# 네이버 증권 페이지에 접속하여
# 해당 페이지의 HTML 문서를 반환
url = "https://finance.naver.com/"
html = req.urlopen(url)
soup = bs(html, 'html.parser')

#print(soup)

tag_table = soup.select("h3.h_popular + table")
#print(len(tag_table))
#print(tag_table)
#print(type(tag_table))

items = tag_table[0].select("tbody th")

for item in items :
    print(item.text)
















