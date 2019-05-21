# -*- coding: utf-8 -*-

# 생성자 존재하는 부모 클래스
class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color    
    def showInfo(self) :
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")
        
class Dog (Animal) :    
    pass

class Cat (Animal) :
    pass

# 부모클래스에 생성자가 정의된 경우, 생성자도 상속되기 때문에
# 자식클래스의 객체를 생성할 때, 부모클래스의 생성자 매개변수를
# 전달해야 합니다.
dog = Dog("강아지", 5, "갈색")
cat = Cat("고양이", 7, "흰색")

dog.showInfo()
cat.showInfo()












