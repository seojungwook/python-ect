# -*- coding: utf-8 -*-

# Set 타입 내부의 데이터 접근방법
set_01 = set("Hello World")

# Set 타입은 기본적으로 데이터의 접근을 
# 허용하지 않습니다.
# Set 내부의 데이터를 리스트 타입으로 변환하 후,
# 인덱스를 사용하여 접근할 수 있습니다.

# Set 타입을 List 타입으로 변환하는 코드
list_01 = list(set_01)

print(set_01)
print(list_01)

# List 타입으로 변환된 이후에는 인덱스를 
# 사용하여 각 데이터에 접근할 수 있음.
print(list_01[0])
print(list_01[1])
print(list_01[2])








