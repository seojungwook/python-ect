# -*- coding: utf-8 -*-

# 기본 입력(키보드 입력)을 처리하는 방법
# input 함수를 사용하여 키보드로부터 입력받을 수 있음
# 변수명 = input()
# 변수명 = input("Message")

# num = input()
num = input("정수를 입력하세요 : ")
print(f"num -> {num}")

# input 함수의 결과는 문자열 타입으로 반환됩니다.
# 만약 input 함수의 결과를 정수로 활용하려면
# 형변환 과정을 거쳐야만 합니다.
# 문자열 -> 정수 : int, 
# 문자열 -> 실수 : float, 
# 문자열 -> 진리형 : bool 을 활용합니다
# 문자열로 형변환을 하기 위해서는 str을 활용합니다.
"""
# 문자열로 정의된 10이 숫자 10으로 변경된 후
# intValue로 대입
intValue = int("10")
# 문자열로 정의된 15.751이 실수 15.751로 변경된 후
# floatValue 대입
floatValue = float("15.751")
# 정수형 타입인 intValue가 문자열로 변환되어
# strValue 대입
strValue = str(intValue)
# 실수형 타입인 floatValue 문자열로 변환되어
# strValue 대입
strValue = str(floatValue)
"""
num = int(num)

if num % 2 == 0 :
    print(f"{num} 정수는 짝수 입니다.")

if num % 2 == 1 :
    print(f"{num} 정수는 홀수 입니다.")










