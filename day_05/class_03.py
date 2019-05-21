# -*- coding: utf-8 -*-

class Person :
    # 클래스 변수
    # 클래스 변수는 클래스 내부에 선언된 변수로써
    # 모든 객체들이 공유하게 되는 변수입니다.
    # 클래스 변수는 단 하나만 생성되며, 모든 객체들은
    # 클래스이름.클래스변수명 으로 접근할 수 있습니다.
    # 만약 클래스변수명과 동일한 인스턴스 변수가 없다면
    # self.클래스변수명 으로 값을 꺼내올수 있습니다.
    name = "Person Class's Name"
    age = "Person Class's Age"    
    address = "Person Class's Address" 
    
    def setInfo(self, name, age, address) :
        # 인스턴스 변수의 생성 코드
        # 인스턴스 변수는 해당 클래스의 각 객체마다
        # 별도로 생성되는 변수(모든 객체가 공유하지 않음)
        # 인스턴스 변수를 생성하기 위해서
        # self.인스턴스변수명 = 값
        self.name = name
        self.age = age
        self.address = address
        
    def showInfo(self) :
        # 아래의 코드는 인스턴스 변수 name이 존재하지 않으면
        # 클래스 변수 name을 출력하고,
        # 인스턴스 변수 name이 존재한다면 인스턴스 변수
        # name의 값을 출력합니다.
        print(f"name -> {self.name}")
        print(f"age -> {self.age}")
        print(f"address -> {self.address}")
        
        # 클래스 변수에 명시적으로 접근하기 위해서는
        # 클래스명.클래스변수명
        print(f"name -> {Person.name}")
        print(f"age -> {Person.age}")
        print(f"address -> {Person.address}")
    
p1 = Person() 
p1.showInfo()
print("=" * 30)
p1.setInfo("사람1", 22, "서울시 강남")
p1.showInfo()






