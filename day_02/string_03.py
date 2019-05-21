# -*- coding: utf-8 -*-

# 문자열 포맷팅
# 0. 문자열 결합 연산을 사용하는 방법(+)
# 1. % 를 사용하여 문자열 내부의 데이터를 
# 삽입하는 방법
# 2. format 메소드를 사용하여 문자열 내부의 
# 데이터를 삽입하는 방법

n1 = 10
n2 = 5
r = n1 + n2

# 문자열 결합을 사용한 방법
# 반드시 str함수를 사용하여 문자열로 변환해야함
# msg = n1 + " + " + n2 + " = " + r
msg = str(n1) + " + " + str(n2) + " = " + str(r)
print(msg)

# % 를 활용한 문자열 포맷팅 방법
# %d : 정수(십진수의 값)
# %f : 실수
# %c : 하나의 문자 값
# %s : 문자열
msg = "%d + %d = %d" % (n1, n2, r)
print(msg)

msg = "%d %c %d%s%d" % (n1, "+", n2, " = ", r)
print(msg)

# 국어/영어/수학 점수를 저장하고 합계 평균을 출력
kor = 100
eng = 99
mat = 87

total = kor + eng + mat
avg = total / 3

# 자리수를 지정하여 출력하는 예제
# %d 는 전체 자리수를 지정하여 출력할 수 있음
# (-의 값을 입력하면 좌측정렬)
print("국어 : %3d 점" % kor)
print("영어 : %3d 점" % eng)
print("수학 : %-3d 점" % mat)
# %f 는 전체 자리수 그리고 소수점 이하 자리수를
# 제어할 수 있음
print("총점 : %d, 평균 : %.2f" % (total, avg))

# 국어/영어/수학 점수를 저장하고 합계 평균을 출력
kor = 100
eng = 99
mat = 87

total = kor + eng + mat
avg = total / 3
# format 메소드를 활용하여 출력하는 방법
print("국어 : {0:->5} 점".format(kor))
print("영어 : {0:-<5} 점".format(eng))
print("수학 : {0:-^5} 점".format(mat))
print("총점 : {0}, 평균 : {1:.2f}".format(
        total, avg))

# 국어/영어/수학 점수를 저장하고 합계 평균을 출력
kor = 100
eng = 99
mat = 87

total = kor + eng + mat
avg = total / 3
# 파이썬 3.6 이상에서만 사용이 가능한 f 포맷팅
print(f"국어 : {kor:5} 점")
print(f"영어 : {eng:<5} 점")
print(f"수학 : {mat:^5} 점".format(mat))
print(f"총점 : {total:5}, 평균 : {avg:.2f}")









