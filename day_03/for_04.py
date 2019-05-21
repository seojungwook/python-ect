# -*- coding: utf-8 -*-

# 중첩된 반복문
# 반복문 내부에 하위 반복문이 선언되는 형태로
# 외부의 반복문이 1번 수행될 때, 내부의 반복문은
# 전체가 수행됩니다.

for i in range(1,4) :
    
    for j in range(1,4) :
        print(f"i -> {i}, j => {j}")

    print("=" * 15)    
    
print("프로그램 종료")










