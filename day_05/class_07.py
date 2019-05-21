# -*- coding: utf-8 -*-

# 소멸자
# 클래스의 객체가 소멸될 때, 자동으로 호출되는 메소드
# (생성자와 반대의 개념)

# del 변수명
# 에 의해서 객체가 소멸될 때 자동 호출됨

# 클래스 내부에 소멸자를 선언하는 방법
# def __del__(self) :
#   객체의 소멸 시, 수행할 작업(파일, DB 처리 작업)

class Food :
    def __init__(self, name) :
        self.name = name
        
    # 소멸자의 선언
    # Food 클래스의 객체가 소멸되기 직전
    # 자동으로 실행되는 메소드
    def __del__(self) :
        print(f"{self.name} 음식을 다 먹었습니다.")

# 소멸자가 호출되는 시점
# 1. 특정 변수에 새로운 객체가 대입되는 경우
#  - 해당 변수가 저장하고 있는 기존의 객체는 소멸됨
food = Food("짜장면")
food = Food("돈까스")

# 2. del을 사용하여 객체를 소멸하는 경우
del food

food_1 = Food("짜장면")
food_2 = Food("치킨")
food_3 = Food("돈까스")

# food_1 객체의 삭제(소멸)
del food_1
# food_2 객체의 삭제(소멸)
del food_2
# food_3 객체의 삭제(소멸)
del food_3








