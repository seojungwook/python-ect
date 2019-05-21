# -*- coding: utf-8 -*-

# 반복문과 else 구문
# 반복문과 else 구문을 조합할 수 있으며
# else 구문은 반복문이 종료되는 시점에 호출됩니다.
# (반복문의 조건식이 False 가 되는 시점에 호출)

num = 1

while num <= 100 :
    print(f"num -> {num:3}")
    num += 1
else:
    # 반복문의 조건식이 거짓이 되어 반복이
    # 종료되면 호출되는 else 영역
    # (반복문이 정상적으로 종료되었음을 의미)
    print("while 반복문 종료")
    
print("프로그램 종료")











