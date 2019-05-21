# -*- coding: utf-8 -*-

import tensorflow as tf

x_data = [1.,2,3,4,5]
y_data = [0.,0,1,1,1]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.ones([1]))
B = tf.Variable(tf.zeros([1]))

#H = X * W + B
# 참/거짓의 분류를 위한 활성화 함수 적용
# simoid 함수 : 입력된 데이터를 0 ~ 1 사이로 압축
H = tf.sigmoid(X * W + B)

# 정답이 1인 케이스의 오차 계산
#loss_1 = Y * tf.log(H)
# 정답이 0인 케이스의 오차 계산
#loss_0 = (1-Y) * -tf.log(H)

#loss = -tf.reduce_mean(Y * tf.log(H) + (1-Y) * -tf.log(H))
loss = -tf.reduce_mean(Y * tf.log(H) + (1-Y) * tf.log(1-H))

train = tf.train.GradientDescentOptimizer(
        learning_rate=0.01).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(1,100001) :
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 100 == 0 :
        loss_v = sess.run(loss, feed_dict={X:x_data, Y:y_data})
        print(f"{step} : {loss_v}")

#print(sess.run(H, feed_dict={X:x_data,Y:y_data}))
#print(sess.run(loss_1, feed_dict={X:x_data,Y:y_data}))
#print(sess.run(loss_0, feed_dict={X:x_data,Y:y_data}))
#print(sess.run(loss, feed_dict={X:x_data,Y:y_data}))















