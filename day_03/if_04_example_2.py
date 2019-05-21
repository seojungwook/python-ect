# -*- coding: utf-8 -*-

# 사용자에게 3과목의 성적을 입력받아
# 평균점수가 90점이상이면 합격, 미만이면 
# 불합격을 출력하세요.

# 1. 입력
num1 = num2 = num3 = 0
#num1 = int(input("1 번째 성적 입력 : "))
#num2 = int(input("2 번째 성적 입력 : "))
#num3 = int(input("3 번째 성적 입력 : "))

numbers = input("3개의 성적 입력(공백을 넣으세요) : ")
numbers_split = numbers.split()
num1 = int(numbers_split[0])
num2 = int(numbers_split[1])
num3 = int(numbers_split[2])

# 2. 처리
# 총점
total = num1 + num2 + num3
# 평균
avg = total / 3
# 합격/불합격 메세지
output = ""
if avg >= 90 :
    output = "합격"
else :
    output = "불합격"

# 3. 출력
print(f"당신의 성적은 {avg:.2f}, '{output}' 입니다.")















