# -*- coding: utf-8 -*-

# 구구단의 실행 결과를 저장하는 리스트 생성하세요.
# (홀수단에 해당되는 결과만 저장)

# 중첩된 반복문을 활용하여 리스트의 값을 추가
#list_gugudan = []
#for i in range(2,10) :
#    # 1
#    if i % 2 :
#        for j in range(1,10) :
#            # 2
#            if i % 2 == j % 2
#            list_gugudan.append(i*j)

list_i = range(2,10)
list_j = range(1,10)

# 리스트 변수의 선언에 중첩된 for 문이 활용되는 예제
# (각 반복문에 조건식을 지정하는 경우)
# 리스트변수명 = [실행문 실행문의 if문 else문 외부의 for문 외부의 if문 
#                           내부의 for문 내부의 if문]
list_gugudan = [i * j if i*j > 10 else 0 for i in list_i if i % 2
                for j in list_j if i % 2 == j % 2]  
     
print(list_gugudan)







