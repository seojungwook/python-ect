# -*- coding: utf-8 -*-

# https://movie.naver.com/movie/sdb/rank/rmovie.nhn 
# 으로부터 영화 랭킹 정보를 수집하세요
"""
1. 사바하
2. 증인
3. 극한직업
...
"""
import urllib.request as req
from bs4 import BeautifulSoup as bs

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = req.urlopen(url)
soup = bs(html, 'html.parser')       

#print(soup)
target = soup.find_all("div", 
                       attrs={"class":"tit3"},
                       limit=10)

for index, data in enumerate(target) :
    data = str(data.text)    
#    if index < 10 :
    print(f"{index + 1} : {data.strip()}")
#    else :
#        break
    
    
    
    
    
    
    
    
    
    
    