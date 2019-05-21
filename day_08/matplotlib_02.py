# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data*random()+5, x))

# 선의 색상을 바꾸기 위한 방법
# plot 함수의 3번째 매개변수를 사용하여 변경
# r : 빨간색, b : 파란색, g : 초록색 등등
# k : 검은색
plt.plot(x,y,"r")

plt.show()














