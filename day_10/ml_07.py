# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

xy = np.loadtxt("diabetes.csv", delimiter=",", dtype=np.float32)
print(xy.shape)

# 학습을 위한 데이터(70%)
x_train = xy[:int(len(xy) * 0.7),:-1]
y_train = xy[:int(len(xy) * 0.7), [-1]]
# 중간 테스트를 위한 데이터(20%)
x_test = xy[int(len(xy) * 0.7):int(len(xy) * 0.9),:-1]
y_test = xy[int(len(xy) * 0.7):int(len(xy) * 0.9), [-1]]
# 학습이 종료된 이후 검증을 위한 데이터(10%)
x_valid = xy[int(len(xy) * 0.9):,:-1]
y_valid = xy[int(len(xy) * 0.9):, [-1]]

X = tf.placeholder(tf.float32, shape=[None, 8])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([8,1]))
B = tf.Variable(tf.zeros([1]))

H = tf.sigmoid(tf.matmul(X, W) + B)

loss = -tf.reduce_mean(Y * tf.log(H) + (1-Y) * tf.log(1-H))

train = tf.train.GradientDescentOptimizer(
        learning_rate=0.0001).minimize(loss)

predicted = tf.cast(H >= 0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(1,1000001) :
    sess.run(train, feed_dict={X:x_train,Y:y_train})
    
    if step % 100 == 0 :
        loss_v, acc_v = sess.run([loss, accuracy], feed_dict={X:x_test,Y:y_test})
        print(f"{step} : {loss_v:.5f}, {acc_v}")

loss_v, acc_v = sess.run([loss, accuracy], feed_dict={X:x_valid,Y:y_valid})
print(f"Result : {loss_v:.5f}, {acc_v}")













