# -*- coding: utf-8 -*-

# 다양한 클래스의 작성 시, 중복되는 정보가
# 발생됨. 이러한 경우 아래와 같이 코드를 
# 복사하는 방식으로 구현하게 됨.
# 클래스의 수정 시, 동일한 분류의 클래스들은
# 같은 수정을 반복하게 됨.
"""
class Dog :
    name = "강아지"
    age = None
    color = None
    address = None

class Cat :
    name = "고양이"
    age = None
    color = None
    address = None
"""

# 클래스의 상속
# 클래스의 재활용을 위한 문법
# 기존에 작성된 클래스의 내용을 코드를 복사하는
# 것이 아닌 문법으로 재활용할 수 있도록 함

# 상속을 활용한 강아지, 고양이 클래스의 선언
# is a 관계를 만족하는 경우 사용할 수 있는 문법
# Dog is a Animal
# Cat is a Animal

# 부모클래스 Animal 선언
# 모든 자식 클래스들이 가져야하는 
# 공통정보, 기능을 포함하는 클래스
class Animal :
    name = "동물"
    age = None
    color = None
    
    def showInfo(self) :
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"color -> {self.color}")
    
# 상속관계를 구현하는 Dog 클래스의 선언
# class 클래스명 (부모클래스명)
class Dog (Animal) :
    # pass 키워드는 구현 코드를 미루기 위해서
    # 사용되는 키워드
    pass

class Cat (Animal) :
    pass

dog = Dog()
cat = Cat()

# Dog, Cat 클래스의 객체는 부모클래스인
# Animal 클래스로부터 물려받은 멤버들을
# 활용할 수 있습니다.
dog.showInfo()
cat.showInfo()






