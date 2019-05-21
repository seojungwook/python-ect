# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data*random()+5, x))

# 선의 타입을 변경하기 위한 방법
# plot 함수의 3번째 매개변수를 사용하여 변경
# - : 일반라인, -- : 대쉬라인, -. : 대쉬-닷라인 등등
# o : Circle Marker
plt.plot(x,y,"--b")

plt.show()














