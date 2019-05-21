import requests
from bs4 import BeautifulSoup

def capycat(Max_page):
    page = 1
    while page <= Max_page:
        url = 'http://creativeworks.tistory.com/' + str(page)
        source = requests.get(url)
        source_text = source.text
        
        soup = BeautifulSoup(source_text , 'html.parser')
        for grep_list in soup.find_all(['h3','class']):
            glist = grep_list.text
            href = url
            print(href)
            print(glist)
        page +=1   
        
        
capycat(10)    