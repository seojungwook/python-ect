# -*- coding: utf-8 -*-

import json

# 파일에 출력하기 위한 딕셔너리 변수
json_data = {}

name = input("이름을 입력 : ")
# 입력된 이름 정보를 딕셔너리에 추가
json_data["name"] = name

age = int(input("나이를 입력 : "))
# 입력된 나이 정보를 딕셔너리에 추가
json_data["age"] = age

address = input("주소를 입력 : ")
# 입력된 주소 정보를 딕셔너리에 추가
json_data["address"] = address

# 입력된 변수를 JSON 포맷의 문자열로 생성
print(json.dumps(json_data))
print(json.dumps(json_data, 
                 ensure_ascii=False, 
                 sort_keys=True, 
                 indent=4))


json_file = "json_example_02.json"
with open(json_file, "w", encoding="utf8") as f :
    json.dump(json_data, f)

json_file = "json_example_02_indent.json"
with open(json_file, "w", encoding="utf8") as f :
    json.dump(json_data, f, 
              ensure_ascii=False, 
              sort_keys=True, 
              indent=4)













