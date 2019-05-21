# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from random import random

x1 = list(range(1,11))
y1 = list(map(lambda data : data*random()+5, x1))

x2 = list(range(1,11))
y2 = list(map(lambda data : data*random()+10, x2))

plt.figure(figsize=(15, 10))

plt.subplot(2,2,1)
plt.title("Plot Example 1")
plt.xlabel("1 ~ 10")
plt.ylabel("Random Data")
plt.plot(x1,y1,"--or",label="First Data")
plt.legend(loc="best", fontsize=25)

plt.subplot(224)
plt.title("Plot Example 4")
plt.xlabel("1 ~ 10")
plt.ylabel("Random Data")
plt.plot(x2,y2,"-.og",label="Second Data")
plt.legend(loc="best")

plt.show()














