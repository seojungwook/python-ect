# -*- coding: utf-8 -*-

try :
    n1 = int(input("정수 입력 : "))
    n2 = int(input("정수 입력 : "))
    r = n1 / n2
# except 영역에서 발생된 예외의 메세지를 처리하는 방법
# except 예외타입(에러타입) as 변수명(메세지를 전달받을 변수) :
except ZeroDivisionError as msg :
    print(f"Error MSG -> {msg}")
else :
    print(f"r -> {r}")
finally :
    print("프로그램 종료")    