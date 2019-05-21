# -*- coding: utf-8 -*-

# 리스트의 데이터 수정 및 삭제
# 리스트의 데이터의 수정은 인덱스 연산을
# 통해서 처리할 수 있습니다.

numbers = [1,2,3,4,5]
print(numbers)

# 인덱스를 사용해서 값을 수정하는 방법
numbers[3] = 40
print(numbers)

# 리스트의 인덱스 연산을 사용하여
# 하위 리스트를 추가할 수 있습니다.
numbers[3] = [41,42,43]
print(numbers)

# 만약 리스트의 특정 위치에 새로운 
# 리스트가 아닌 다수개의 데이터를 추가
# 하려는 경우 슬라이싱 연산을 적용해야
# 합니다.
numbers[3:4] = [41,42,43]
print(numbers)

# 리스트 내부의 데이터를 삭제하는 방법
# del 연산자 사용
del numbers[4]
print(numbers)

del numbers[3:5]
print(numbers)

# 리스트의 메소드를 활용한 삭제 방법
# remove, pop 메소드
numbers.append(2)
print(numbers)

# 리스트 내부에서 2 데이터를 삭제
# remove 메소드를 활용하여 특정 데이터를
# 삭제할 수 있음. 단 최초에 발견된 한개만 삭제
numbers.remove(2)
print(numbers)

# 리스트의 마지막 요소를 제거
# pop 메소드는 리스트의 마지막 요소를 반환하고
# 제거하는 특징
pop_value = numbers.pop()
print(numbers)
print(f"제거된 값은 {pop_value} 입니다.")






















