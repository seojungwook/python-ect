# -*- coding: utf-8 -*-

# Set 타입의 데이터
# 내부의 데이터 중복을 허용하지 않는 타입
# Dictionary와 차이점은 키 값이 존재하지 않음
# 내부 데이터의 저장 순서를 유지하지 않음

# 변수명 = set()
# 변수명 = set(초기값으로 저장할 데이터)
set_01 = set()
print(f"set_01's type -> {type(set_01)}")
print(f"set_01's size -> {len(set_01)}")

print("=" * 22)
set_02 = set([1,2,3])
print(f"set_02's size -> {len(set_02)}")
print(f"set_02 -> {set_02}")

print("=" * 22)
set_03 = set([1,1,2,2,3,3])
print(f"set_03's size -> {len(set_03)}")
print(f"set_03 -> {set_03}")

print("=" * 22)
# Set 타입에 문자열 타입을 저장하는 경우
# 해당 문자열 구성하고 있는 각 문자값으로 저장됨
# 이때 중복은 제거되고, 순서가 유지되지 않음
set_04 = set("Hello World")
print(f"set_04's size -> {len(set_04)}")
print(f"set_04 -> {set_04}")







