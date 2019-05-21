# -*- coding: utf-8 -*-

class Food :
    # 인스턴스 변수의 생성을 위한 메소드 선언
    # (각각의 객체마다 생성되는 변수를 선언)
    def init(self, name, price) :        
        self.name = name
        self.price = price
    # 인스턴스 변수의 값을 출력하기 위한 메소드
    def showInfo(self) :
        print(f"name -> {self.name}")
        print(f"price -> {self.price}")
        
food = Food()
# 클래스의 객체를 생성한 후, 인스턴스 변수를 생성하는
# 메소드를 호출하지 않았기 때문에 아래의 메소드 호출은
# 에러가 발생됩니다.
# food.showInfo()
food.init("짜장면", 5000)
food.showInfo()








        
        
        
        
        
        