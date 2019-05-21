# -*- coding: utf-8 -*-

# 두개의 정수와 나눗셈 연산의 결과를 저장하기 위한 리스트 변수
# numbers = []
numbers = list()

try :
    # 첫번째 정수 입력 후, 리스트에 추가
    #temp = int(input("첫번째 정수 : "))
    numbers.append( int(input("첫 번째 정수 : ")) )
    
    # 두번째 정수 입력 후, 리스트에 추가
    #temp = int(input("두번째 정수 : "))
    numbers.append( int(input("첫 번째 정수 : ")) )
    
    # 입력된 데이터 확인
    #print(numbers)
    
    # 첫번째 입력된 정수 / 두번째 입력된 정수의 결과를 저장
    numbers.append(numbers[0] / numbers[1])
    
    print(f"{numbers[0]} / {numbers[1]} = {numbers[2]}")
# 여러 타입의 예외를 처리하기 위한 방법
# except 첫번째 예외 타입 as 변수명
#   첫번째 예외 타입이 발생한 경우의 실행 코드
# except 두번째 예외 타입 as 변수명
#   두번째 예외 타입이 발생한 경우의 실행 코드
# except Exception as 변수명
#   상단에 위치한 except 에서 예외가 처리되지 못한 경우
#   실행할 실행 코드
except ZeroDivisionError :
    print("ZeroDivisionError 에러 발생")
except ValueError as msg :
    print(f"ValueError 에러 발생 - {msg}")
except Exception as msg : 
    print(f"에러 발생 - {msg}")









