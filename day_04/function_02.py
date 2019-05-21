# -*- coding: utf-8 -*-

# 매개변수가 활용되는 함수의 선언
# 매개변수란 함수의 실행에 필요한 값을 의미합니다.
# (기존의 변수와 동일한 개념)
# def 함수명( 매개변수명1, 매개변수명2, ... )

# 매개변수를 1개 전달받아 실행할 수 있는 
# showNumber 함수를 선언
def showNumber(number) :
    # 함수를 정의하게 되면 반드시 몸체(실행문)를
    # 선언해야만 합니다.
    # 만약 차후에 함수의 실행 코드를 작성하는 경우
    # pass 를 사용하여 에러를 방지할 수 있습니다.
    # pass
    
    # 매개변수는 변수와 동일하게 사용할 수 있습니다.
    # 매개변수는 함수가 실행(호출)될 때 생성되며
    # 전달된 매개변수로 초기화 됩니다.
    print(f"number -> {number}")

# 매개변수가 지정된 함수는 반드시 매개변수의 값을
# 전달해야만 호출할 수 있습니다.
# showNumber()

showNumber(11)

# 두개의 매개변수가 선언된 plus 함수의 선언
# plus 함수를 실행하기 위해서는 반드시 2개의 값을
# 전달해야만 합니다.
def plus(n1, n2) :
    print(f"{n1:2} + {n2:2} = {n1 + n2:2}")

# 매개변수를 전달하여 함수를 실행하는 코드
# 매개변수는 전달하는 위치에 맞게 대입됩니다.
# 10 은 n1 매개변수에 대입, 20은 n2 매개변수에 대입됨
plus(10, 20)
    
    
    
    
    
    
    
    
    
    