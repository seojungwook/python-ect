# -*- coding: utf-8 -*-

# 파이썬에서는 대소문자를 구분합니다.
msg = "Hello"
Msg = "Python"

print(f"msg -> {msg}")
print(f"Msg -> {Msg}")

# 하나의 실행문으로 다수개의 변수를 
# 서로 다른 값으로 초기화 할 수 있습니다.
n1 = 10
n2 = 5
print(f"n1 = {n1}, n2 = {n2}")

n1, n2 = 100, 50
print(f"n1 = {n1}, n2 = {n2}")

# SWAP 처리
# 서로 다른 두 변수의 값을 변경하는 방법
# n1과 n2의 값을 서로 교환

# 기존의 SWAP 방식
# 임의의 변수를 생성한 후, 값을 교환
#temp = n1
#n1 = n2
#n2 = temp

n1, n2 = n2, n1
print(f"n1 = {n1}, n2 = {n2}")

# 값의 대입 시, _ 사용하게 되면 처리하지 않겠다는
# 의미로 사용
_, n2 = n2, n1
print(f"n1 = {n1}, n2 = {n2}")















