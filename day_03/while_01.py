# -*- coding: utf-8 -*-

# 제어문 - 반복문
# 특정 영역에 위치한 실행문을 조건식에 따라 
# 반복할 수 있는 문법
# (조건식이 거짓이 될 때까지 반복)

# while 문
# while 조건식 :
#   반복해서 실행할 문장(조건식이 참일 경우)

num = 1

while num <= 10 :
    print(f"num -> {num:2}")
    
    # 반복문을 종료하기 위한 num 변수의 값 수정
    # num = num + 1
    # 변형된 형태의 대입연산자
    # 자기 자신에 연산한 결과를 대입받을 수 있는
    # 대입연산자
    # 아래의 코드는 num = num + 1 과 동일함
    num += 1
    
print("프로그램 종료")











