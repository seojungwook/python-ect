# -*- coding: utf-8 -*-

# 논리연산자
# 다수개의 관계식의 결과(진리형값)을 하나의 진리형의
# 결과로 반환하는 연산자

# 1. and 연산자
# L        R       RESULT
# FALSE    FALSE   FALSE
# FALSE    TRUE    FALSE
# TRUE     FALSE   FALSE
# TRUE     TRUE    TRUE
print("{} and {} = {}".format(
        False, False, False and False))
print("{} and {} = {}".format(
        False, True, False and True))
print("{} and {} = {}".format(
        True, False, True and False))
print("{} and {} = {}".format(
        True, True, True and True))

# 2. or 연산자
# L        R       RESULT
# FALSE    FALSE   FALSE
# FALSE    TRUE    TRUE
# TRUE     FALSE   TRUE
# TRUE     TRUE    TRUE
print("{} or {} = {}".format(
        False, False, False or False))
print("{} or {} = {}".format(
        False, True, False or True))
print("{} or {} = {}".format(
        True, False, True or False))
print("{} or {} = {}".format(
        True, True, True or True))

# 3. not 연산자
# not False => True
# not True  => False
print("not {} = {}".format(
        False, not False))
print("not {} = {}".format(
        True, not True))

# 나이 정보
age = 33
# 성별(1,3 -> 남자:2,4 -> 여자)
gender = 2

# 나이가 20대 또는 30이면서 성별이 여자인
# 경우를 판단하는 식을 작성하고 결과를 
# print 로 확인하세요.

# 값의 범위를 지정하여 참/거짓 판단
# e1 = age >= 20 and age < 30
# 10 의 자리의 수를 추출하여 나이 판단
e1 = age // 10 == 2
e2 = age // 10 == 3
# 20대 이거나 30대 인 경우를 판단
flag_age = e1 or e2
# 성별을 판단
flag_gender = gender == 2 or gender == 4
# 최종 결과
flag_result = flag_age and flag_gender
print(flag_result)














