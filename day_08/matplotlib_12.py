# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x = list(range(1,11))
y = list(map(lambda data : data*random()+5, x))

plt.title("Bar Chart Example")

plt.xlabel("1 ~ 10")
plt.ylabel("Random Data")

# BAR 형태의 차트 생성 방법
# bar, barh 함수를 사용
# bar(가로방향), barh(세로방향)
# bar(x데이터, y데이터)
# 참고사이트
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar

# color 속성은 색상 지정
# 기본값은 blue
# alpha 속성은 투명도 지정
# (0 ~ 1)
plt.bar(x,y,color="red",alpha=0.3)

plt.show()














