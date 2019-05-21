# -*- coding: utf-8 -*-

# 리스트 데이터에 대한 슬라이싱 연산
# 리스트 내부의 특정 영역의 데이터를 복제할 수 있는 연산
# 변수명[시작인덱스:종료인덱스]
numbers = [1,2,3,4,5,6,7,8,9]
numbers_part = numbers[2:7]

print(numbers)
print(numbers_part)

# 슬라이싱을 통해서 분리된 데이터는 완전 복제로 구성되어
# 원본 데이터에는 영향이 없습니다.
numbers_part[0] = 30
print(numbers)
print(numbers_part)








