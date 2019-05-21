# -*- coding: utf-8 -*-

# 구구단 전체를 출력할 수 있는 gugudan_all 함수를 선언하고 
# 호출 결과를 확인하세요.
def gugudan_all() :
    for i in range(2, 10) :
        print(f"{i}단을 출력합니다.")
        for j in range(1, 10) :
            print(f"{i} * {j} = {i*j}")
        print()
        
# gugudan_all()

# 매개변수로 전달받은 구구단을 출력할 수 있는 gugudan_one 함수를 
# 선언하고 호출 결과를 확인하세요.
def gugudan_one(i) : 
    print(f"{i}단을 출력합니다.")
    for j in range(1, 10) :
        print(f"{i} * {j} = {i*j}")
    print()

gugudan_one(7)
        
        
        










        