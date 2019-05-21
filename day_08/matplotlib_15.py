# -*- coding: utf-8 -*-

from random import random
from matplotlib import pyplot as plt

x = list(range(1,1001))
x = list(map(lambda data : str(data), x))

y = [int(1000 * random()) for data in x]

plt.title('Scatter example')
plt.xlabel("x : 1 ~ 1000")
plt.ylabel("y : random * 1000")

#plt.plot(x, y)
#plt.bar(x, y)
# 스캐터 플롯 - 산점도
# 값의 분포를 선이 아닌 점의 형태로 출력하는 그래프
# 참고사이트
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter
plt.scatter(x, y)
plt.show()















