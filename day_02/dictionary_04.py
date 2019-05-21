# -*- coding: utf-8 -*-

# Dictionary 내부의 데이터를 리스트로
# 변환하는 방법
numbers = { "One":1, "Two":2, "Three":3 }
# 딕셔너리에 저장된 모든 키값을 반환하는
# keys 메소드
numbers_keys = numbers.keys()
print(numbers_keys)
# keys 메소드의 반환 결과를 리스트 타입으로
# 변환하는 코드
numbers_keys = list(numbers_keys)
print(numbers_keys)

# 딕셔너리에 저장된 모든 키값을 반환하는
# values 메소드
numbers_values = numbers.values()
print(numbers_values)
# values 메소드의 반환 결과를 리스트 타입으로
# 변환하는 코드
numbers_values = list(numbers_values)
print(numbers_values)





