# -*- coding: utf-8 -*-

# Dictionary 데이터에서 값을 추출하는 방법
numbers = { "One":1, "Two":2, "Three":3 }

print(f'numbers["Two"] -> {numbers["Two"]}')
# [] 를 사용하여 값을 추출하는 경우 해당 키 값이
# 존재하지 않으면 에러가 발생됩니다.
# print(f'numbers["Five"] -> {numbers["Five"]}')

# Dictionary의 get메소드를 활용하여 값을 추출하는 경우
# 해당 키값이 존재하지 않을때 None 값을 반환합니다.
target_value = numbers.get("Two")
print(f'numbers["Two"] -> {target_value}')
# 아래는 Five 키값이 존재하지 않기 때문에
# None 값이 반환됨
target_value = numbers.get("Five")
print(f'numbers["Five"] -> {target_value}')






