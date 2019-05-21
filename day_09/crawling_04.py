# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs

html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=136872" 
            title="미녀와 야수">미녀와 야수</a>
    </div>
</td>
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=167099" 
            title="사바하">사바하</a>
    </div>
</td>

'''

soup = bs(html, 'html.parser')

# 접근연산자 또는 find 메소드는 
# 첫번째 발견된 문서 정보만 추출
#tag_a = soup.a
#print(tag_a)
#tag_a = soup.find(name="a")
#print(tag_a)

# BeautifulSoup 객체의 find_all 메소드
# 특정 태그, 또는 태그와 속성의 조합이 
# 다수개인 경우 활용할 수 있음
# find 메소드와 달리 동일한 형태의 태그를
# 모두 검색하여 리스트 형태로 반환
tag_a = soup.find_all(name="a")
print(tag_a)
print(f"검색된 a 태그의 개수 : {len(tag_a)}")
print(f"검색된 첫번째 a 태그의 텍스트 : {tag_a[0].text}")
print(f"검색된 두번째 a 태그의 텍스트 : {tag_a[1].text}")

for tag in tag_a : 
    print(tag.text)
    
# 태그의 CSS 선택자 정보를 활용하여 검색하는 방법
# select, select_one 메소드를 활용
# 아래의 경우 div 태그 하위에 위치한 a 태그를 검색
tag_a = soup.select(".tit3 > a")    
print(tag_a)






















