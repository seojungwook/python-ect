# -*- coding: utf-8 -*-

# 구구단의 실행 결과를 저장하는 리스트 생성하세요.

# 중첩된 반복문을 활용하여 리스트의 값을 추가
#list_gugudan = []
#for i in range(2,10) :
#    for j in range(1,10) :
#        list_gugudan.append(i*j)

list_i = range(2,10)
list_j = range(1,10)

# 리스트 변수의 선언에 중첩된 for 문이 활용되는 예제
# 리스트변수명 = [실행문 외부의 for문 내부의 for문]
list_gugudan = [i * j for i in list_i
                for j in list_j]    
    
print(list_gugudan)







