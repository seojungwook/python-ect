# -*- coding: utf-8 -*-

# for 반복문은 정해진 횟수의 반복을 제어하는 경우 사용
# 특정 범위의 반복을 수행(리스트, 딕셔너리, Set 타입의 크기)

# for 변수명 in 컬렉션변수 : 
# 컬렉션 변수의 시작부터 끝까지 각 데이터를 추출하여
# 변수에 대입한 후 실행됨

# 리스트 타입의 컬렉션을 for 반복문으로 제어하는 방법
numbers = [1,2,3,4,5]
for data in numbers :
    print(f"data -> {data}")
    
print("=" * 15)

# 딕셔너리 타입의 컬렉션을 for 반복문으로 제어하는 방법
numbers = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}

# 딕셔너리 타입 변수의 items 메소드는 key, value의 쌍으로
# 반환하는 메소드
# for 반복에서 key, value 의 값을 동시에 전달받을 수 있
for key, value in numbers.items():
    print(f"key -> {key}, value -> {value}")

# 딕셔너리 타입의 컬렉션을 for 문으로 반복하면 내부의
# 키 값들이 반환됩니다.
#for data in numbers:
#    # 딕셔너리 타입의 변수에서 키값을 활용하여 Value를 추출
#    # 1. [] 연산 - 반드시 존재하고 있는 Key 값만 사용
#    #  - 만약 존재하지 않는 Key 값이면 에러 발생
#    # 2. get 메소드
#    #  - 만약 존재하지 않는 Key 값이면 None 값 반환
#    #  - 에러 발생 X    
#    print(f"key -> {data}, value -> {numbers[data]}")
#    print(f"key -> {data}, value -> {numbers.get(data)}")
    
print("=" * 15)

# Set 타입의 컬렉션을 for 반복문으로 제어하는 방법
msg = set("Hello Python~!")
for char in msg :
    print(f"char -> '{char}'")

print("=" * 15)







