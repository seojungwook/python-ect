# -*- coding: utf-8 -*-

import json

with open("json_example_01.json", "r") as json_file :
    # json 모듈의 load 함수를 사용하여
    # 파일로부터 JSON 포맷의 데이터를 읽어올 수 있음
    json_data = json.load(json_file)
    
    # 문자열
    # key가 json_string인 Value 추출
    json_string = json_data["json_string"]
    print(json_string, type(json_string))
    
    # 숫자
    # key가 json_number인 Value 추출
    json_number = json_data["json_number"]
    print(json_number, type(json_number))
    
    # 리스트
    # key가 json_list인 Value 추출
    json_list = json_data["json_list"]
    print(json_list, type(json_list))
    
    for index, data in enumerate(json_list) :
        print(f"{index} : {data}")
    
    # 딕셔너리
    # key가 json_dict인 Value 추출
    json_dict = json_data["json_dict"]
    print(json_dict, type(json_dict))
    
    for key, value in json_dict.items() : 
        print(f"{key} : {value}")
    
    # bool형
    # key가 json_bool인 bool형 자료 가져오기
    json_bool = json_data["json_bool"]
    print(json_bool, type(json_bool))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    