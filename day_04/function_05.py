# -*- coding: utf-8 -*-

# 두개 이상의 값을 반환하는 함수의 선언
def max_and_min(n1, n2) :
    # 함수의 내부에서는 변수를 선언하여
    # 사용할 수 있습니다.
    maxValue = minValue = n1
    
    if n2 > maxValue :
        maxValue = n2
    
    if minValue > n2 :
        minValue = n2
    
    # 2개의 값을 반환하는 return 문
    # (다수개의 값을 반환하더라도, 컬렉션(튜플) 
    # 타입으로 반환되기 때문에 1개의 변수로 
    # 값을 전달받을 수 있습니다.)
    return maxValue, minValue

# 컬렉션(튜플) 타입으로 리턴 값을 전달받는 경우
r = max_and_min(100, 200)
print(f"r -> {type(r)}")
print(f"r -> {r}")        

# 리턴되는 값을 각 변수에 대입받는 경우
# return 키워드 이후에 선언된 순서로
# 변수에 대입됩니다.
r1, r2 = max_and_min(100, 200)
print(f"r1 -> {r1}, r2 -> {r2}") 

# 리턴되는 값 보다 많은 개수의 변수에는
# 대입받을 수는 없습니다.
#r1, r2, r3 = max_and_min(100, 200)
#print(f"r1 -> {r1}, r2 -> {r2}, r3 -> {r3}") 

# 함수의 리턴값을 사용하지 않는 경우,
# _ 로 변수를 대치할 수 있습니다.
# _ 로 선언하는 경우 사용하지 않는 값이됨
r1, _ = max_and_min(100, 200)
_, r2 = max_and_min(100, 200)
_, _ = max_and_min(100, 200)










        