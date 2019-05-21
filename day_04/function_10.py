# -*- coding: utf-8 -*-

# 지역변수와 전역변수 그리고 함수
# 지역변수 : 함수 내부에 선언된 모든 변수
# 전역변수 : 함수 외부에 선언된 모든 변수

# 전역변수로 선언된 변수는 함수 내부에서 
# 자유롭게 접근할 수 있는 변수입니다.
# (접근할 수는 있지만 추가적인 선언이 필요함)

# 전역변수 선언
count = 0

def setCount(num) :
    # 지역변수 이름과 전역변수 이름이 동일한경우
    # 지역변수가 우선시 됩니다.
    # 아래는 지역변수 count 를 생성하고
    # 지역변수 count 변수에 매개변수의 값을 할당
    # 전역변수의 값은 변경이 없음
    count = num
    
def addCount() :
    # global 키워드는 함수 내부에서 전역변수에 
    # 접근하기 위한 키워드
    # global 전역변수명
    # global로 선언된 변수는 전역변수의 값을
    # 수정할 수 있는 변수입니다.
    global count
    count += 1

print(f"count -> {count}")
setCount(5)
print(f"count -> {count}")
addCount()
print(f"count -> {count}")






