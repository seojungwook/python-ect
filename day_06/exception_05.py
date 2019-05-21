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
# Exception 클래스
# 모든 예외의 최상위 부모 클래스 타입
# Exception 클래스의 타입은 어떠한 예외 타입이 전달되어도
# 값을 받을 수 있는 타입으로 모든 예외를 처리할 수 있습니다.
except Exception as msg :
    print(f"Error MSG -> {msg}")
else :
    print(f"r -> {r}")
finally :
    print("프로그램 종료")    