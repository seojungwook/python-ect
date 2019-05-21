# -*- coding: utf-8 -*-

# 다중상속을 구현하는 클래스의 선언
# 파이썬의 클래스는 다수개의 클래스를 동시에 상속받을 수 있음
# class 자식클래스명 (부모1, 부모2, ... 부모N)
class PlusCalculator :
    def plus(self, n1, n2) : 
        print(f"{n1} + {n2} = {n1 + n2}")
        
class MinusCalculator :
    def minus(self, n1, n2) : 
        print(f"{n1} - {n2} = {n1 - n2}")
        
class MulCalculator :
    def mul(self, n1, n2) : 
        print(f"{n1} * {n2} = {n1 * n2}")   
        
class DivCalculator :
    def div(self, n1, n2) : 
        print(f"{n1} / {n2} = {n1 / n2}") 
        
# 사칙연산을 제공하는 Calculator 클래스(다중상속을 구현)
# 다중 상속을 구현하는 클래스의 선언
# 파이썬은 다중 상속을 지원하며, 
# 특정 클래스는 다수개의 클래스로부터 속성, 기능을
# 물려받을 수 있습니다.
# class 클래스명 (부모클래스1, 부모클래스2 ... )
class Calculator (PlusCalculator, MinusCalculator, MulCalculator, DivCalculator) :
    pass

cal = Calculator()

cal.plus(22, 10)
cal.minus(22, 10)
cal.mul(22, 10)
cal.div(22, 10)
        
# 인스턴스 변수를 포함하는 CalculatorWithAttr 클래스 선언
# 1. 상속을 구현하는 경우
"""
class CalculatorWithAttr (Calculator) : 
    # 인스턴스 변수의 선언을 위한 생성자
    def __init__(self, n1, n2) :
        self.n1 = n1
        self.n2 = n2
    # 부모클래스의 메소드를 오버라이딩
    def plus(self) :
        # 부모클래스의 메소드 호출을 통한 기능 구현
        super().plus(self.n1, self.n2)
    def minus(self) :
        super().minus(self.n1, self.n2)
    def mul(self) :
        super().mul(self.n1, self.n2)
    def div(self) :
        super().div(self.n1, self.n2)
"""    
# 2. 상속을 구현하지 않고, Calculator 클래스의 객체를
# 멤버 필드로 활용하는 방법
class CalculatorWithAttr : 
    # 인스턴스 변수의 선언을 위한 생성자
    def __init__(self, n1, n2) :
        # 외부에서의 접근을 차단한 Calculator 객체 생성
        self.__calculator = Calculator()
        self.n1 = n1
        self.n2 = n2    
    def plus(self) :
        # 멤버 필드로 가지고 있는 Calculator 클래스의 
        # 객체를 활용한 기능 구현
        self.__calculator.plus(self.n1, self.n2)
    def minus(self) :
        self.__calculator.minus(self.n1, self.n2)
    def mul(self) :
        self.__calculator.mul(self.n1, self.n2)
    def div(self) :
        self.__calculator.div(self.n1, self.n2)
        
calculator = CalculatorWithAttr(22, 10)
calculator.plus()
calculator.minus()
calculator.mul()
calculator.div()

# isinstance 함수
# 특정 변수가 특정 클래스 타입의 객체인지 
# 확인할 수 있는 함수
# isinstance(변수명, 클래스명)

# 동일한 클래스 타입의 객체는 True 가 반환됩니다.
print( isinstance(Calculator(), Calculator) )
# 서로 다른 클래스 타입의 객체는 False 가 반환됩니다.
print( isinstance(CalculatorWithAttr(1,2), Calculator) )
# 서로 다른 클래스라도 상속관계를 구현하고 있는 경우
# 자식클래스는 부모클래스로 인식될 수 있습니다.
# isinstance(자식클래스의객체, 부모클래스명) -> True
print( isinstance(Calculator(), PlusCalculator) )
# 부모클래스는 자식클래스로 인식될 수 없습니다.
# isinstance(부모클래스의객체, 자식클래스명) -> False
print( isinstance(PlusCalculator(), Calculator) )





        
        
        
        
        
        