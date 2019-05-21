# -*- coding: utf-8 -*-

# for 반복문
# for 변수명 in 컬렉션타입의데이터 :
#   컬렉션타입의데이터를 하나씩 추출하여 작업할 내용...

# range 함수
# 1. range(max)
#  - range(5) -> [0,1,2,3,4]
# 2. range(start, max)
#  - range(2, 5) -> [2,3,4]
# 3. range(start, max, step)
#  - range(1, 10, 2) -> [1,3,5,7,9]

for i in range(10) :
    print(f"i -> {i:2}")

print("=" * 10)

for i in range(5, 10) :
    print(f"i -> {i:2}")

print("=" * 10)

for i in range(1, 10, 3) :
    print(f"i -> {i:2}")

print("=" * 10)

total = 0
for i in range(1, 101) :
    total += i
    
print(f"1 ~ 100까지의 합계는 {total} 입니다.")












