# -*- coding: utf-8 -*-

# 문제 1번의 실행 결과와 소스 코드 제출
# 실행 결과는 콘솔/이미지

import tensorflow as tf
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression

x_data = [10., 20, 30, 40, 50]
y_data = [95., 203, 293, 397, 503]

plt.title("Data Set")
plt.xlabel("Input Data")
plt.ylabel("Label Data")
plt.plot(x_data, y_data, "ro")
plt.show()

X = tf.placeholder(dtype=tf.float32)
Y = tf.placeholder(dtype=tf.float32)

# 난수를 사용하여 가중치 변수를 선언
# W = tf.Variable(tf.random_normal([1]))
# 0으로 가중치 변수를 초기화
W = tf.Variable(tf.zeros([1]))

H = X * W

#loss = H - Y
#loss = tf.square(H - Y)
loss = tf.reduce_mean(tf.square(H - Y))

# 손실값을 개선하기 위한 경사하강법 구현 객체
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_list = []
for step in range(1, 10001) :
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    loss_list.append(sess.run(loss, feed_dict={X:x_data, Y:y_data}))
    if step % 100 == 0 :
        loss_v = sess.run(loss, feed_dict={X:x_data, Y:y_data})
        print(f"{step} : {loss_v}")
        
h_v = sess.run(H, feed_dict={X:x_data})
plt.title("Data Set")
plt.xlabel("Input Data")
plt.ylabel("Label Data")
plt.plot(x_data, y_data, "ro")
plt.plot(x_data, h_v, "b-")
plt.show()

plt.title("Loss Trend")
plt.xlabel("Count")
plt.ylabel("Loss Data")
plt.plot([i for i in range(1, 10001)], loss_list, "r--")
plt.show()

#h_v = sess.run(H, feed_dict={X:x_data, Y:y_data})
#print(h_v)
#
#plt.title("Data Set")
#plt.xlabel("Input Data")
#plt.ylabel("Label Data")
#plt.plot(x_data, y_data, "ro")
#plt.plot(x_data, h_v, "bo")
#plt.show()
#
#loss_v = sess.run(loss, feed_dict={X:x_data, Y:y_data})
#print(loss_v)

#print(sess.run(X, feed_dict={X:x_data}))
#print(sess.run(Y, feed_dict={Y:y_data}))













