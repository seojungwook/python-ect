# -*- coding: utf-8 -*-

# 리스트 데이터는 결합될 수 있습니다.
list_front = [1,2,3,4,5]
list_end = [6,7,8,9]

list_merge = list_front + list_end
print(list_merge)

# + 연산을 통한 리스트의 결합은 완전 복제를
# 구현하고 있습니다.
# 아래와 같이 복제된 데이터를 수정해도
# 원본 데이터에는 변화가 없습니다.
list_merge[0] = 10
print(list_front)
print(list_end)
print(list_merge)

# 리스트의 반복 연산
# * 연산자를 사용하여 리스트의 내용을 
# 반복하여 저장할 수 있습니다.
numbers = [1,2,3]
numbers = numbers * 3

print(numbers)










