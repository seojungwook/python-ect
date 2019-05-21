# -*- coding: utf-8 -*-

# 반복문과  break 키워드, else 영역
# 반복문에 else 영역이 정의된 경우 
# 반복문의 조건식이 False로 처리되면 반복이 
# 종료된 후, else 영역으로 이동되어 else 영역이
# 실행됩니다.
# 단, 반복문 내부에서 break 키워드를 통해 
# 종료되는 경우(강제종료) else 영역이 실행되지
# 않습니다.

# 반복문의 else 영역은 반복의 정상적인 종료 시
# 처리할 실행 코드를 정의하는 공간입니다.

num = 1

while num <= 3:
    isExit = input("강제 종료(y/n)? : ")
    if( isExit == "y" or isExit == "Y" ):
        break 

    num += 1
else :
    print("while 문이 정상적으로 종료됨")
    
print("프로그램 종료")



