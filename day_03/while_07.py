# -*- coding: utf-8 -*-

# 반복문과 continue 키워드
# 반복문 내부에서 continue 키워드는 현재의 실행을 
# 중지하고 다음 반복으로 이동하기 위해서 사용
# (반복을 강제 종료하는 것이 아님)
# (반복문의 종료 지점으로 이동하여 다음 반복으로 이동)

# 1 ~ 100까지 정수 중 짝수만 출력하세요.

num = 1

while num <= 100 :
    if num % 2 == 1 :
        num += 1
        continue
    
    print(f"num -> {num:3}")    
    num += 1













