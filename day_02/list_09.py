# -*- coding: utf-8 -*-

# 리스트 내부의 데이터를 검색하는 방법
# index 메소드를 활용할 수 있습니다.
numbers = [1,2,3,4,5,6,7,8,9]
# 인덱스 메소드는 해당 리스트에서 
# 매개변수로 전달된 값을 검색하여
# 인덱스의 값을 반환합니다.
target_index = numbers.index(7)
print(target_index)

# index 메소드는 매개변수의 값을
# 리스트에서 찾을 수 없다면 에러가
# 발생됩니다.
# 아래의 0을 검색하는 코드는 에러가 발생
# target_index = numbers.index(0)
# print(target_index)

# 리스트 변수의 count 메소드는 매개변수의
# 값이 리스트에 저장된 개수를 반환
# 0이라면 존재하지 않음 
# - 0인경우 index를 사용하면 안됨..
target_count = numbers.count(7)
print(target_count)












