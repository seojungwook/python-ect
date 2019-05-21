# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

from bs4 import BeautifulSoup as bs
import urllib.request as req

class CrawlingThread (Thread) :
    def __init__(self, name, url, sleepTime) :
        self.url = url
        self.sleepTime = sleepTime
        # 외부에서 쓰레드의 종료 여부를 확인할 수 
        # 있도록 변수를 지정
        self.isEnd = False
        # 쓰레드의 이름을 지정하기 위해서 
        # 부모 클래스 Thread의 생성자 활용
        super().__init__(name=name)
    
    def run(self) :     
        while True :
            try :
                html = req.urlopen(self.url)
                soup = bs(html, 'html.parser')
                tag_table = soup.select("h3.h_popular + table")
                items = tag_table[0].select("tbody th")
                
                for item in items :
                    print(item.text)
                    
                sleep(self.sleepTime)
            except Exception as msg :
                print(f"Error : {msg}")
                self.isEnd = True
                break
        
# 현재 파일이 실행되는 경우에만 아래의 코드가 실행
if __name__ == "__main__" :
    myCrawlingThread = CrawlingThread("Stock", "https://finance.naver.com/", 5)
    myCrawlingThread.start()
    
    while True : 
        
        if myCrawlingThread.isEnd :
            print("문제가 발생하여 쓰레드가 종료됨")
            break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    