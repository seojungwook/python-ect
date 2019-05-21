# -*- coding: utf-8 -*-

try :
    n1 = int(input("정수 입력 : "))
    n2 = int(input("정수 입력 : "))
    r = n1 / n2
# 여러 타입의 예외를 처리하기 위해서는 
# except 구문을 다수개 작성하여 처리할 수 있습니다.
except ZeroDivisionError as msg :
    # / 0 을 하는 경우 실행되는 영역
    print(f"Error MSG -> {msg}")
except ValueError as msg :
    # 잘못된 입력이 들어온 경우 실행되는 영역
    print(f"Error MSG -> {msg}")
else :
    print(f"r -> {r}")
finally :
    print("프로그램 종료")    