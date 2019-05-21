# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs

html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=136872" 
            title="미녀와 야수">미녀와 야수</a>
    </div>
</td>
'''

soup = bs(html, 'html.parser')

# 각 태그에 지정된 속성값의 접근
# attrs 속성
# 해당 태그에 지정된 속성값을 Dictionary 타입으로 반환
# BeautifulSoup변수.attrs -> {태그속성들...}
# BeautifulSoup변수.attrs["속성이름"] -> 속성값
tag_td = soup.td
#print(tag_td)
print(tag_td.attrs)
print(tag_td.attrs["class"])
print(tag_td.attrs["class"][0])

tag_a = soup.a
print(tag_a.attrs)
print(tag_a.attrs["href"])
print(tag_a.attrs["title"])















