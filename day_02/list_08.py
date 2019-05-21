# -*- coding: utf-8 -*-

# 리스트 데이터 요소를 추가하는 방법
# 1. append 메소드를 활용
#  - 리스트의 마지막에 데이터를 추가
# 2. insert 메소드를 활용
#  - 리스트의 특정 인덱스 자리에 데이터를 추가
numbers = [1,3,5]

# numbers 리스트에 7을 추가
# numbers = numbers + [7]
numbers.append(7)
print(numbers)

# numbers 리스트에 8,9를 추가
# append 메소드는 매개변수를 1개만 사용
# numbers.append(8,9)

# 아래와 같이 append 메소드를 사용하면
# 리스트 변수가 추가됩니다.
# numbers.append( [8,9] )

# 여러개의 데이터를 리스트의 끝에 추가하려면
# 리스트 결합을 사용해야 합니다.
numbers = numbers + [8,9]
print(numbers)

# 리스트의 특정 인덱스에 데이터 삽입
numbers.insert(1, 2)
print(numbers)

numbers.insert(3, 4)
print(numbers)

numbers.insert(5, 6)
print(numbers)






