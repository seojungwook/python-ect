# -*- coding: utf-8 -*-

# 임의의 로또번호를 생성 (100개)
# 임의의 생성된 로또번호를 조사하여 각 숫자의 빈도수를 
# Bar 차트로 출력

from random import random

lotto_count = 100
# 각 6개로 구성된 로또번호들의 리스트를 저장하는 변수
lotto_numbers = []

for _ in range(lotto_count) :
    # 임의로 생성된 로또 번호를 저장하기 위한 변수
    lotto = set()
    while len(lotto) < 6 :
        # 1 ~ 45 사이의 숫자를 생성하여
        # SET 내부에 추가
        # (중복 데이터를 추가되지 않음)
        lotto.add(int(random() * 45) + 1)
    lotto_list = list(lotto)
    lotto_list.sort()
    lotto_numbers.append(lotto_list)
    
#print(lotto_numbers)
    
# 1 ~ 45까지의 정수값을 가지는 리스트 생성
x = list(range(1,46))
x = list(map(lambda data : str(data), x))
#  0으로 초기화된 크기 45의 리스트 변수
y = [0] * 45

#print(x)
#print(y)

for lotto in lotto_numbers :
    for index in lotto :
        # 해당되는 숫자의 리스트 자리에 1을 증가
        y[index-1] += 1

from matplotlib import pyplot as plt

plt.figure(figsize=(13,8))
plt.title("Lotto Number Counting")
plt.xlabel("Number")
plt.ylabel("Counting")

plt.plot(x, y, "ro-.")
plt.bar(x, y, color="green")
plt.show()














