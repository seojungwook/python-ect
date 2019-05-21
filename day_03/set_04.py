# -*- coding: utf-8 -*-

numbers = set([1,2,3,4,5,6,7,8,9])
print(f"numbers -> {numbers}")

# Set 내부의 데이터를 삭제하는 방법
# 1. remove 메소드를 사용
#  - 특정 데이터를 삭제하려는 경우
#  - 삭제하는 기능만 실행
numbers.remove(5)
print(f"numbers -> {numbers}")

r_value = numbers.remove(8)
print(f"numbers -> {numbers}")
# remove 메소드는 삭제만 지원합니다.
# 삭제한 데이터는 소멸됨(반환되지 않음)
print(f"r_value => {r_value}")

# Set 내부에 존재하지 않는 데이터는 
# 삭제할 수 없습니다.(실행 에러가 발생)
#numbers.remove(0)
#print(f"numbers -> {numbers}")

# 2. pop 메소드를 사용
#  - 특정 데이터를 삭제하려는 경우
#    (Set 내부에 저장된 가장 앞쪽의 데이터)
#  - Set 내부에서 데이터를 삭제하고, 
#    삭제한 데이터를 반환하는 기능
r_value = numbers.pop()
print(f"numbers -> {numbers}")
print(f"r_value -> {r_value}")

# pop 메소드는 임의의 특정 데이터를 삭제할 수 없음
#r_value = numbers.pop(6)
#print(f"numbers -> {numbers}")
#print(f"r_value -> {r_value}")

# 3. clear 메소드를 사용
#  - Set 내부의 전체 데이터 삭제
numbers.clear()
print(f"numbers -> {numbers}")







