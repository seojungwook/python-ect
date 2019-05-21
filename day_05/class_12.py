# -*- coding: utf-8 -*-

# 더하기 기능을 제공하는 PlusCalculator 클래스
# 를 작성하세요.
# PlusCalculator 클래스는 plus 메소드가 제공되며
# 정수 타입 두개를 매개변수로 전달받아
# 덧셈의 결과를 출력합니다.

class PlusCalculator :
    def plus(self, n1, n2) : 
        print(f"{n1} + {n2} = {n1 + n2}")

plusCal = PlusCalculator()
plusCal.plus(22, 11)

# Minus 기능을 추가한 PlusMinusCalculator 클래스
class PlusMinusCalculator (PlusCalculator) :
    def minus(self, n1, n2) : 
        print(f"{n1} - {n2} = {n1 - n2}")

plusMinusCal = PlusMinusCalculator()
plusMinusCal.plus(22, 11)
plusMinusCal.minus(22, 11)










