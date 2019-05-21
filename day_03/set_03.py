# -*- coding: utf-8 -*-

# Set 타입에 데이터를 추가하는 방법
# 1. add 메소드를 사용하는 방법
#  - add 메소드는 단일 데이터를 추가

# 비어있는 Set 변수를 생성
numbers = set()
print(f"numbers's size -> {len(numbers)}")

# 단일 데이터를 추가하는 add 메소드
# Set 내부의 데이터 개수가 증가하는 것을
# 확인할 수 있습니다.
numbers.add(10)
print(f"numbers's size -> {len(numbers)}")
numbers.add(11)
print(f"numbers's size -> {len(numbers)}")
numbers.add(12)
print(f"numbers's size -> {len(numbers)}")
numbers.add(13)
print(f"numbers's size -> {len(numbers)}")

# 중복된 데이터는 추가될 수 없습니다.
numbers.add(13)
print(f"numbers's size -> {len(numbers)}")

print(f"numbers -> {numbers}")

# 2. update 메소드를 사용하여 데이터를 
#   추가하는 방법
#  - 다수개의 데이터를 추가할 수 있는 방법
numbers.update([14,15,16,17,18,19])

print(f"numbers's size -> {len(numbers)}")
print(f"numbers -> {numbers}")

















