# -*- coding: utf-8 -*-

# Dictionary 내부의 데이터를 삭제하는 방법
numbers = { "One":1, "Two":2, "Three":3 }
print(numbers)
print(len(numbers))

# Dictionary 내부의 데이터를 삭제하기 이전에
# 키값의 존재유무를 확인하는 방법
# in 연산자를 활용하여 처리
isThree = "Three" in numbers
print(f"isThree -> {isThree}")
isFive = "Five" in numbers
print(f"isFive -> {isFive}")

# del 연산자를 통해서 하나의 키값 데이터를 삭제
# 주의사항
# 존재하지 않는 키값을 사용하는 경우 에러가 발생
del numbers["Three"]
print(numbers)
print(len(numbers))

# clear 메소드를 통해서 전체 데이터를 삭제
numbers.clear()
print(numbers)
print(len(numbers))











