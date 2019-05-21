# -*- coding: utf-8 -*-

# if ~ else 구문
# if 문의 조건식이 거짓일 경우 else 문을 활용하여
# 처리하는 방법

# if 조건식:
#   조건식이 참일경우 실행될 문장
# else:
#   조건식이 거짓일경우 실행될 문장

#num = input("정수를 입력 : ")
#num = int(num)

# input 함수의 결과를 정수로 변환하여 num 변수에 대입
num = int(input("정수를 입력 : "))

if num % 2 == 0 :
    print(f"{num} 정수는 짝수입니다.")
else :
    # if 문의 조건식이 거짓일 경우 실행
    print(f"{num} 정수는 홀수입니다.")











