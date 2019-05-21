# -*- coding: utf-8 -*-

from urllib.request import urlopen

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Mont-Blanc_from_Planpraz_station.jpg/1200px-Mont-Blanc_from_Planpraz_station.jpg"

with urlopen(url) as response :
    # urlopen의 결과 변수에 대해서 read 메소드를 호출하여
    # 이미지 데이터를 추출
    content = response.read()
    
    fileName = "./download_02.jpg"
    with open(fileName, "wb") as f :
        # 이미지 데이터를 파일에 저장
        f.write(content)