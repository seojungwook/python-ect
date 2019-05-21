# -*- coding: utf-8 -*-

# 구구단 클래스를 작성하세요.
# 구구단 클래스에는 두개의 메소드를 포함합니다.
# printAll 메소드와 printOne 메소드
# printAll 메소드는 매개변수가 없으며, 호출되면
# 전체 구구단을 출력
# printOne 메소드는 하나의 정수형 매개변수가 
# 있으며, 호출되면 전달된 매개변수의 구구단 출력

class Gugudan :
    def printAll(self) :
        for i in range(2, 10) :
            # 동일한 클래스 내부의 메소스 사이에서 
            # 호출하는 예제
            self.printOne(i)
            print()
    
    def printOne(self, dan) :
        print(f"{dan} 단을 출력합니다.")
        for j in range(1, 10) :
            print(f"{dan} * {j} = {dan * j}")

gugudan = Gugudan()
gugudan.printAll()
#gugudan.printOne(5)







