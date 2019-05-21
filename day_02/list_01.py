# -*- coding: utf-8 -*-

# LIST 타입의 데이터
# 기존의 배열과 동적 배열을 의미하는 데이터
# 다수개의 데이터를 하나의 변수로 제어할 수 있음

# 리스트 변수를 생성하는 방법
# [] 를 사용
# 1. 빈 리스트 변수를 생성
list_1 = []
list_1 = list()
# 2. 초기값을 가지는 리스트 변수를 생성
list_2 = [1, 2, 3, 4, 5]
# 3. 서로 다른 타입의 초기값을 가지는 
# 리스트 변수를 생성
list_3 = [1, "2", 3.5, False, 5]

# 리스트 내부의 요소 개수를 확인하는 방법
size = len(list_1)
print(f"list_1's size -> {size}")
size = len(list_2)
print(f"list_2's size -> {size}")
size = len(list_3)
print(f"list_3's size -> {size}")

# 리스트 내부의 각 요소에 접근하는 방법
# 인덱스 연산 사용
# 시작은 0, 마지막 요소의 인덱스는 -1
print(f"list_2[0] -> {list_2[0]}")
print(f"list_2[1] -> {list_2[1]}")
print(f"list_2[-1] -> {list_2[-1]}")
print(f"list_2[-2] -> {list_2[-2]}")








