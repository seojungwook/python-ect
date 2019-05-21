# -*- coding: utf-8 -*-

# 3과목의 성적을 입력받아 총점과 평균
# 그리고 등급을 출력하세요
# 90점 이상 A, 80점 이상 B, 70점 이상 C,
# 60점 이상 D, 그 외에는 F

# 1. 입력
numbers = input("3개의 성적 입력(공백을 넣으세요) : ")
numbers_split = numbers.split()
num1 = int(numbers_split[0])
num2 = int(numbers_split[1])
num3 = int(numbers_split[2])

# 2. 처리
total = num1 + num2 + num3
avg = total / 3
grade = "?"

if avg > 100 or avg < 0 :
    grade = "?"
elif avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"    
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"
    
print(f"총점 : {total}점, 평균 : {avg:.2f}점")

if grade != "?" :
    print(f"평가 : '{grade}' 등급")
else:
    print("성적 점수를 확인하세요")









