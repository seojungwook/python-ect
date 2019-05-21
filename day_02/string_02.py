# -*- coding: utf-8 -*-

# 슬라이싱 연산
# 베열/리스트에 해당되는 데이터에 적용할 수 있는 연산
# 배열/리스트의 임의의 지점의 값을 추출할 수 있음
# 변수명[ 시작인덱스 : 종료인덱스 ]
msg = "Hello Python~!"
# msg 문자열 변수에서 Python 문자열만 추출하는 슬라이싱
msg_part = msg[6:12]
print("msg_part -> {}".format(msg_part))

# msg 문자열 변수에서 Hello 문자열만 추출하는 슬라이싱
msg_part = msg[0:5]
print("msg_part -> {}".format(msg_part))

# 위의 예제와 같이 처음부터 시작하여 슬라이싱하는 경우
# 0 은 생략이 가능합니다.
msg_part = msg[:5]
print("msg_part -> {}".format(msg_part))

# 또한 마지막 인덱스까지 슬라이싱 하는 경우 마지막 인덱스
# 는 생략할 수 있습니다.
msg_part = msg[6:]
print("msg_part -> {}".format(msg_part))

# 배열과 리스트 변수에는 마지막 인덱스를 의미하는 -1 값을
# 사용할 수 있습니다.
# -1 값을 사용하여 슬라이싱하는 경우 마지막 열(행)은 제외
msg_part = msg[:-1]
print("msg_part -> {}".format(msg_part))











