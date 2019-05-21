# -*- coding: utf-8 -*-

import urllib.request as req
from bs4 import BeautifulSoup as bs

import os

try:
    if not (os.path.isdir("./download/")) :
        os.makedirs(os.path.join("./download/"))
except :    
    print("Failed to create directory!!!!!")    

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = req.urlopen(url)
soup = bs(html, 'html.parser')       

target = soup.find_all("div", 
                       attrs={"class":"tit3"},
                       limit=10)

for index, data in enumerate(target) :
    # 링크 정보 추출을 위한 A 태그 정보 추출
    tag_a = data.a
    # 파일의 이름을 지정하기 위한 text 정보 추출
    filename = os.path.join("./download/", str(tag_a.text) + ".jpg")
    #filename = str(tag_a.text) + ".jpg"        
    # print(f"{index + 1} : {filename}")
    
    # 영화 정보 페이지의 URL 변수
    movie_info_page_url = "https://movie.naver.com" + tag_a.attrs["href"]    
    # print(movie_info_page_url)

    # 상세 영화 정보 페이지로 접근하여 BS 객체 생성
    movie_info_html = req.urlopen(movie_info_page_url)
    movie_info_soup = bs(movie_info_html, 'html.parser')     
    
    poster_img_tag = movie_info_soup.select_one("div.poster > a > img")
    #print(poster_img_tag)
    #print(poster_img_tag.attrs["src"])
    
    img_url = str(poster_img_tag.attrs["src"])
    target_index = img_url.index("?")
    img_url = img_url[:target_index]    
    # print(img_url)

    # 파일 다운로드 실행    
    with req.urlopen(img_url) as response :
        content = response.read()
        with open(filename, "wb") as f :
            # 이미지 데이터를 파일에 저장
            f.write(content)
    
    
    
    
    
    
    
    
    
    
    
    
    
    