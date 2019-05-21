# -*- coding: utf-8 -*-

# list_1의 홀수 요소에는 10을 곱하고, 짝수 요소는 그대로 전달하여
# list_2를 생성하세요
list_1 = [11,22,33]

# 리스트의 크기만큼 반복을 수행하면서
# 조건식이 만족하는 경우 list_2에 데이터를 추가
#list_2 = []
#for i in range( len(list_1) ) :
#    if list_1[i] % 2 == 1 :
#        list_2.append(list_1[i] * 10)
#    else :
#        list_2.append(list_1[i])

# 리스트 변수의 선언에 for 문이 활용되는 예제
# (특정 조건에 만족하는 경우와 만족하지 않는 경우를 처리하는 방식)
# 리스트변수명 = [실행문 if 조건식 else 거짓인경우의값 for 변수명 in 컬렉션]
list_2 = [data * 10 if data % 2 == 1 else data for data in list_1]

print(f"list_1 -> {list_1}")
print(f"list_2 -> {list_2}")












