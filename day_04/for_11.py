# -*- coding: utf-8 -*-

# list_1의 홀수 요소에 10을 곱하여 list_2를 생성하세요
list_1 = [11,22,33]
list_2 = []

# 리스트의 크기만큼 반복을 수행하면서
# 조건식이 만족하는 경우 list_2에 데이터를 추가
#for i in range( len(list_1) ) :
#    if list_1[i] % 2 == 1 :
#        list_2.append(list_1[i] * 10)

# 리스트 변수의 선언에 for 문이 활용되는 예제
# (특정 조건에 만족하는 경우)
# 리스트변수명 = [실행문 for 변수명 in 컬렉션 if 조건식]
list_2 = [data * 10 for data in list_1 if data % 2 == 1]

print(f"list_1 -> {list_1}")
print(f"list_2 -> {list_2}")







