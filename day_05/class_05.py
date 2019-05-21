# -*- coding: utf-8 -*-

class UpdateFood :
    # 클래스의 생성자
    # __init__ 메소드
    # 클래스의 생성자는 클래스의 객체 생성시
    # 자동으로 호출되는 메소드
    # 각 객체가 생성될 때마다 실행됨
    # 생성자에서 필요한 매개변수를 객체 
    # 생성 시 전달하지 않으면 에러가 발생
    
    # 생성자를 사용하는 경우 인스턴스 변수의 생성을
    # 보장할 수 있습니다.(반드시 호출되는 메소드이므로)
    # 그리고 불필요한 메소드 호출을 방지할 수 있습니다.
    def __init__(self, name, price) :        
        self.name = name
        self.price = price
        
    # 인스턴스 변수의 값을 출력하기 위한 메소드
    def showInfo(self) :
        print(f"name -> {self.name}")
        print(f"price -> {self.price}")

food = UpdateFood("햄버거", 7000)
food.showInfo()