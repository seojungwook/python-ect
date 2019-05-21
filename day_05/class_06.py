# -*- coding: utf-8 -*-

# 클래스 멤버의 접근지정자
# 객체지향의 정보은닉의 개념을 구현 (private 키워드)
# 파이썬 언어에서는 접근지정자의 개념이 
# 존재하지 않음

# __ 를 활용한 접근이 제한된 인스턴스 변수 선언
# __변수명 으로 정의할 수 있으며, 외부에서 접근할 수
# 없는 인스턴스 변수를 선언할 수 있음
# 값을 접근할 수 없고, 값을 수정할 수 없음
# __ 가 선언된 변수는 되도록 외부에서 접근하지 않도록
# 주의해야함.
class Account:    
    def __init__(self) :        
        self.__balance = 0
    
    def deposit(self, money) :
        self.__balance += money
        
    def withraw(self, money) :
        self.__balance -= money
    
    def showInfo(self):
        print(f"현재 잔고는 {self.__balance}원 입니다.")
a = Account()
# __ 로 선언된 변수는 접근할 수 없습니다.
#print(a.__balance)
# 아래의 코드는 생성자에서 선언된 __balance 와 
# 다른 변수를 생성하는 코드입니다.
a.__balance = 10000
# 위의 코드에서 __balance가 10000으로 대입되었지만
# 생성자에서 선언된 __balance와는 다른 변수이므로
# 값의 변경이 일어나지 않습니다.
a.showInfo()

# 생성자에서 선언된 __balance를 수정하기 위해서는
# 메소드를 통해서만 가능합니다.
a.deposit(5000)
a.showInfo()





