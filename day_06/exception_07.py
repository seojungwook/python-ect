# -*- coding: utf-8 -*-

class Calculator :
    def __init__(self) :
        # 아래의 코드는 숫자가 입력되지 않는 경우
        # 예외가 발생합니다.
        # 예외처리를 활용하여 숫자가 들어올때까지
        # 값을 입력받도록 수정하세요.
        
        # 계산에 사용될 인스턴스 변수
        # (각각의 객체마다 별도로 생성되는 변수)
        while True :
            try :
                self.n1 = int(input("첫 번째 정수 : "))
            except : 
                print("숫자 타입만 입력해야합니다.")
            else :
                break
        
        while True :
            try :
                self.n2 = int(input("두 번째 정수 : "))
            except : 
                print("숫자 타입만 입력해야합니다.")
            else :
                break  
        
        # 계산 결과를 저장하기 위한 변수
        self.result = None
    
    def display(self, operator) :
        print(f"{self.n1} {operator} {self.n2} = {self.result}")
    
    def plus(self) :
        self.result = self.n1 + self.n2
        self.display("+")
    
    def minus(self) :
        self.result = self.n1 - self.n2
        self.display("-")
        
cal = Calculator()
cal.plus()
cal.minus()
        
        
        
        
        
        
        
        
        
        