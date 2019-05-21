# -*- coding: utf-8 -*-

# 상속관계를 구현하고 있는 자식클래스의 오버라이딩 문법
# 부모로부터 상속받은 생성자, 메소드를 자식 클래스의 용도에
# 맞춰 새롭게 정의하는 문법
class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color    
    def showInfo(self) :
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")

# 소리를 낼 수 있는 강이지 클래스의 선언
class Dog (Animal) :  
    # 소리 정보를 추가적으로 받아들일수 있는 생성자 오버라이딩
    def __init__(self, name, age, color, sound) :  
        # 자식클래스에서 부모클래스의 생성자를 
        # 사용하지 않고 새롭게 생성자를 정의하는 경우
        # 부모클래스의 생성자를 명시적으로 호출하여
        # 부모클래스의 인스턴스 변수들이 올바르게
        # 생성될 수 있도록 해야합니다.
        
        # super() 함수는 부모클래스에 접근하기 위한
        # 참조값을 반환하는 함수
        # 1. 부모 클래스의 생성자 호출
        # 2. 오버라이딩된 부모클래스의 메소드 호출
        
        # 자식 클래스의 생성자에서 부모 클래스의 생성자를
        # 호출할 수 있습니다.
        # super().__init__(부모클래스 생성자의 매개변수)
        super().__init__(name, age, color)
        self.sound = sound
        
    # 부모클래스로부터 물려받은 showInfo 메소드는
    # sound 값을 출력할 수 없음
    # 이러한 경우 부모클래스를 새롭게 재정의하여
    # 사용할 수 있습니다. (메소드 오버라이딩)
    # 메소드 오버라이딩을 구현하면 부모의 메소드는
    # 무시되고 오버라이딩된 자식클래스의 메소드가
    # 호출됩니다.
    def showInfo(self) :
        # 부모클래스 Animal의 showInfo 메소드 호출
        # super()를 사용하여 부모클래스의 
        # 오버라이딩된 메소드를 호출할 수 있습니다.
        super().showInfo()
        # Dog 클래스의 추가적인 처리 작업
        print(f"소리를 냅니다 - {self.sound}")

# 점프를 뛸 수 있는 고양이 클래스의 선언
class Cat (Animal) :
    # 점프 정보를 추가적으로 받아들일수 있는 생성자 오버라이딩
    def __init__(self, name, age, color, jump) :    
        super().__init__(name, age, color)
        self.jump = jump
        
    def showInfo(self) :
        # 부모클래스 Animal의 showInfo 메소드 호출
        super().showInfo()
        # Cat 클래스의 추가적인 처리 작업
        print(f"점프를 뜁니다 - {self.jump} m")

dog = Dog("강아지", 5, "갈색", "왈왈")
dog.showInfo()
cat = Cat("고양이", 7, "흰색", 3)
cat.showInfo()










