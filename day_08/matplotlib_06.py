# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x1 = list(range(1,11))
y1 = list(map(lambda data : data*random()+5, x1))

x2 = list(range(1,11))
y2 = list(map(lambda data : data*random()+10, x2))

plt.title("Plot Example")

plt.xlabel("1 ~ 10")
plt.ylabel("Random Data")

# 여러 라인을 하나의 그래프에 출력할 수 있음
plt.plot(x1,y1,"--r")
plt.plot(x2,y2,"-.g")

plt.show()














