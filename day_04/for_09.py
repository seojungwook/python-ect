# -*- coding: utf-8 -*-

numbers = [3, 5, 1, 7, 2]

# sort 메소드를 활용하지 않고 
# 오름차순 정렬을 구현하세요.

# 정렬의 기준 인덱스를 정하는 반복문(외부)
for i in range(len(numbers)-1) :
    # 기준 인덱스의 다음 위치부터 시작하여
    # 마지막 요소까지 반복을 수행
    for j in range(i+1, len(numbers)) :
        
        # 오름차순 정렬이므로 i 번째의 값은
        # 항상 작아야함.
        # 만약 기준 위치의 값이 더 크다면
        # 값을 교환함 (SWAP)
        if numbers[i] > numbers[j] :
            # 기존의 SWAP 로직
#            temp = numbers[i]
#            numbers[i] = numbers[j]
#            numbers[j] = temp
            
            # 파이썬에서의 SWAP 로직
            numbers[i], numbers[j] = numbers[j] , numbers[i]

print(numbers)






