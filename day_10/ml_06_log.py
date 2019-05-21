# -*- coding: utf-8 -*-

# 문제 3번의 실행 결과와 소스 코드 제출
# 실행 결과는 이미지

import tensorflow as tf
from matplotlib import pyplot as plt

value = tf.placeholder(tf.float32)
log_value_plus = tf.log(value)
log_value_minus = -tf.log(value)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

start = 0
step = 0.001
log_x = []
log_y = []
while start <= 1 :
    log_x.append(start)
    log_y.append(sess.run(log_value_plus, feed_dict={value:start}))
    start += step
    
plt.title("tf.log")
plt.xlabel("data")
plt.ylabel("log value")
plt.plot(log_x, log_y, "r--")
plt.show()    

start = 0
step = 0.001
log_x = []
log_y = []
while start <= 1 :
    log_x.append(start)
    log_y.append(sess.run(log_value_minus, feed_dict={value:start}))
    start += step
    
plt.title("-tf.log")
plt.xlabel("data")
plt.ylabel("log value")
plt.plot(log_x, log_y, "r--")
plt.show()   
