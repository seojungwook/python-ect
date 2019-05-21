# -*- coding: utf-8 -*-

# 조건이 다수개인 경우 처리하는 방법
# if ~ elif ~ else
# if 1번째 조건식:
#   1번째 조건식이 참일 경우 실행문장
# elif 2번째 조건식:
#   2번째 조건식이 참일 경우 실행문장
# ...
# else:
#   모든 조건식이 거짓일 경우 실행문장

print("1. 한식")
print("2. 일식")
print("3. 중식")
menu = int(input("메뉴를 선택하세요 : "))

output = ""
if menu == 1 :
    output = "한식을 선택"
elif menu == 2 :
    output = "일식을 선택"
elif menu == 3 :
    output = "중식을 선택"
else:
    output = "잘못된 번호를 선택"

print(output)










