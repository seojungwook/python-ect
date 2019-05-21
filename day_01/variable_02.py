# -*- coding: utf-8 -*-

# 문자열 타입의 변수
# (한개 이상의 문자들의 집합)
# ", ', """, '''으로 정의된 데이터

# 쌍따옴표로 정의된 문자열
str_1 = "Hello 1"
# 작은따옴표로 정의된 문자열
str_2 = 'Hello 2'
# """ 으로 정의된 문자열
str_3 = """Hello 3"""
# ''' 으로 정의된 문자열
str_4 = '''Hello 4'''

print("str_1 -> {}".format(str_1))
print("str_2 -> {}".format(str_2))
print("str_3 -> {}".format(str_3))
print("str_4 -> {}".format(str_4))

# 문자열 데이터에 " 를 포함하는 경우
# Hello~ "A"
msg = "Hello~ \"A\""
msg = 'Hello~ "A"'
print(msg)

# 문자열 데이터에 ' 를 포함하는 경우
# Hello~ 'A'
msg = 'Hello~ \'A\''
msg = "Hello~ 'A'"
print(msg)

# 여러 라인으로 이뤄진 문자열을 저장하기 위해서
# """ 가 활용되는 모습
msg = """파이썬[1](영어: Python)은 1991년[2] 
프로그래머인 귀도 반 로섬(Guido van Rossum)[3]이 
발표한 고급 프로그래밍 언어로, 플랫폼 독립적이며 
인터프리터식, 객체지향적, 동적 타이핑(dynamically 
typed) 대화형 언어이다. 파이썬이라는 이름은 귀도가 
좋아하는 코미디 〈Monty Python's 
Flying Circus〉에서 따온 것이다."""












