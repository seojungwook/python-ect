# -*- coding: utf-8 -*-

# 1 ~ 12 사이의 정수를 입력받아 
# 해당 월의 일수를 출력하세요
# EX) 1 -> 31, 2 -> 28, 3 -> 31 ...

# 1. 입력
month = int(input("1 ~ 12 사이의 정수를 입력 : "))

# 2. 처리
day = -1
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
if month in month_31:
    day = 31
elif month in month_30:
    day = 30
elif month == 2:
    day = 28    
else:
    day = -1
    
# 3. 출력
if day != -1:
    print(f"{month} 월은 {day} 일 까지 있습니다.")
else:
    print("1 ~ 12 사이의 정수만 입력할 수 있습니다.")
    











