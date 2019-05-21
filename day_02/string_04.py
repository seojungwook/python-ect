# -*- coding: utf-8 -*-

# 문자열에 적용될 수 있는 함수/메소드

msg = "Hello World~!"

# 문자열의 길이
# len 함수를 사용 (배열/리스트의 개수)
# len(문자열)
print(f"'{msg}' 는 {len(msg)} 글자로 \
      작성되었습니다.")

# 특정 문자열의 위치 확인
# 문자열 변수의 find 메소드 사용
# 변수명.find("검색할문자열")
# 해당 문자열의 시작 인덱스의 값이 반환
i = msg.find("World")
print(f"msg 변수에서 'World' 문자열은 \
      {i} 번째에 위치합니다.")

# 문자열의 공백 제거(엔터키, 띄어쓰기, 탭)
# \n : 개행문자, \t : 탭 문자를 의미
msg = "\n\t   Hello World~!  \n\t"
print(f"normal : {msg}")

# lstrip, rstrip, strip
print(f"lstrip : {msg.lstrip()}")
print(f"rstrip : {msg.rstrip()}")
print(f"strip : {msg.strip()}")

# lstrip, rstrip, strip 메소드는 특정
# 문자를 제거한 결과를 반환하는 메소드
# 기본적으로 공백을 제거할 수 있으며,
# 매개변수에 값을 입력하면 해당 문자를 제거
# 한 문자열을 반환
msg = "Hello World~!"
print(f"lstrip : {msg.lstrip('elH')}")
print(f"rstrip : {msg.rstrip('elH')}")
print(f"strip : {msg.strip('elH')}")

# 문자열 데이터를 변경하는 방법
# replace 메소드
# 변수명.replace("기존문자열", "변경할문자열")
msg = "Hello Python~!"
msg_replace = msg.replace("Python", "C++")
print(msg_replace)

# 문자열 데이터를 나누기위한 방법
# split 메소드를 활용
# 문자열변수.split() -> 공백을 기준으로 나눔
# 문자열변수.split(",") -> ,를 기준으로 나눔
subjects = "kor eng math"
# 공백을 기준으로 나눠진 결과를 리스트로 반환
subject_list = subjects.split()
print(subject_list)

subjects = "kor:eng:math"
# : 을 기준으로 나눠진 결과를 리스트로 반환
subject_list = subjects.split(":")
print(subject_list)

# 아래의 주민번호 문자열에서 생년월일 그리고
# 성별을 의미하는 정수를 추출하세요
jumin = "990120-2012521"

front = jumin[:jumin.find("-")]
end = jumin[jumin.find("-")+1:]

#print(front)
#print(end)

# 성별 정보 추출
gender = end[0]

birth_year = front[:2]
birth_month = front[2:4]
birth_day = front[4:]

print(f"년도 : {birth_year}, \
      월 : {birth_month} \
      일 : {birth_day} \
      성별 : {gender}")














