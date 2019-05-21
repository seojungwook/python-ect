# -*- coding: utf-8 -*-

# 반복문 - for 문
# while 반복문의 경우 조건식을 기준으로 반복을 제어
# (while 문은 불특정한 횟수의 반복을 제어하는 경우에 유용함)
# 만약 특정 리스트, 딕셔너리, Set 내부의 데이터를 순회하는 경우
# while 반복문은 작업을 위한 부가적인 작업들이 발생됨
# (리스트 내부의 데이터를 추출하는 과정 등)

numbers = [1,2,3,4,5,6,7,8,9,10]

# while 문을 사용하여 numbers 리스트를 순회하는 과정
index = 0
size = len(numbers)
while index < size :
    value = numbers[index]
    print(f"numbers[{index}] -> {value:2}")
    
    index += 1
    
print("프로그램 종료 - while")

# for 문을 사용하여 numbers 리스트를 순회하는 과정
for value in numbers :
    print(f"{value:2}")

print("프로그램 종료 - for")









