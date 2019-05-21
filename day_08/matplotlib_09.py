# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x1 = list(range(1,11))
y1 = list(map(lambda data : data*random()+5, x1))

x2 = list(range(1,11))
y2 = list(map(lambda data : data*random()+10, x2))

# 다수개의 그래프를 생성하는 경우
# 서브플롯 설정 방법
# subplot 함수를 사용
# subplot(행,열,위치)
# subplot(행열위치) -> , 없이 사용할 수 있음
plt.subplot(2,2,1)
plt.title("Plot Example 1")
plt.xlabel("1 ~ 10")
plt.ylabel("Random Data")
plt.plot(x1,y1,"--or",label="First Data")
plt.legend(loc="best")

plt.subplot(224)
plt.title("Plot Example 4")
plt.xlabel("1 ~ 10")
plt.ylabel("Random Data")
plt.plot(x2,y2,"-.og",label="Second Data")
plt.legend(loc="best")

plt.show()














