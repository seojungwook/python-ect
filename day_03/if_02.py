# -*- coding: utf-8 -*-

# 특정 제어문의 영역을 선언하기 위해서 들여쓰기를 활용
# 주의사항
# 특정 영역은 다수개의 실행문으로 구성될 수 있으며
# 특정 영역 내부의 모든 실행문은 동일 한 들여쓰기 깊이를
# 가져야만 합니다.

number = 11

# 아래의 실행문 정의는 들여쓰기의 깊이(칸)가 다르기
# 때문에 실행될 수 없습니다.
if number % 2 == 0 :
    print(f"{number} 정수는 짝수 입니다.1")
   print(f"{number} 정수는 짝수 입니다.2")
  print(f"{number} 정수는 짝수 입니다.3")

if number % 2 == 1 :
    print(f"{number} 정수는 홀수 입니다.1")
     print(f"{number} 정수는 홀수 입니다.2")
      print(f"{number} 정수는 홀수 입니다.3")
    
    
    
    
    
    
    
    
    
    
    