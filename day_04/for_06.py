# -*- coding: utf-8 -*-

# 구구단의 짝수단만 출력하는 예제를 작성하세요.
for i in range(2, 10) :   
    
    if i % 2 == 1 :
        continue
        
    print(f"{i} 단을 출력합니다.\n")
    
    for j in range(1,10) :        
        print(f"{i} * {j} = {i*j}")
        
    print()
    