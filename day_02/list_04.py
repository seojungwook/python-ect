# -*- coding: utf-8 -*-

# 파이썬의 모든 변수들은 객체를 참조합니다.
# (실제 데이터가 아닌 데이터의 참조값을 가짐)
# 아래의 numbers 변수는 [1,2,3,4,5] 리스트의
# 저장 위치값을 대입받습니다.
numbers = [1,2,3,4,5]
print(numbers)

# 리스트 변수의 참조값을 복사하는 코드
# numbers_copy 변수는 새로운 리스트를 
# 참조하지 않고 기존의 리스트를 공유합니다.
numbers_copy = numbers
print(numbers)
print(numbers_copy)

# numbers_copy 를 사용하여 리스트 데이터를 
# 수정하면, numbers 변수를 사용해서도 변경된
# 값을 확인할 수 있습니다.
# 얕은복사현상 - 실제 데이터가 분리되지 않고
# 공유되는 현상
numbers_copy[0] = 100
print(numbers)
print(numbers_copy)

# 리스트 데이터의 복제를 위한 슬라이싱 연산
# (주소만 전달하는 것이 아닌 실제 데이터를 복제)
numbers_copy = numbers[:]
numbers_copy[1] = 200
print(numbers)
print(numbers_copy)













