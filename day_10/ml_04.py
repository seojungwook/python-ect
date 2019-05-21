# -*- coding: utf-8 -*-

# 문제 2번의 실행 결과와 소스 코드 제출
# 실행 결과는 콘솔/이미지

import tensorflow as tf

# 입력 데이터의 개수가 2개 이상인 경우의 처리방법
x1_data = [1.,2,3,4,5]
x2_data = [5.,6,7,8,9]
y_data = [35., 55, 77, 89, 100]

X1 = tf.placeholder(tf.float32)
X2 = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([1]))
W2 = tf.Variable(tf.random_normal([1]))
B = tf.Variable(tf.zeros([1]))

H = X1 * W1 + X2 * W2 + B

loss = tf.reduce_mean(tf.square(H - Y))

train = tf.train.GradientDescentOptimizer(
        learning_rate=0.00001).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_list = []
step = 1
loss_v1 = None
loss_v2 = None
while True :
    sess.run(train, feed_dict={X1:x1_data, X2:x2_data, Y:y_data})
    loss_v2 = sess.run(loss, feed_dict={
                                         X1:x1_data, 
                                         X2:x2_data, 
                                         Y:y_data})
    loss_list.append(loss_v2)
    
    if step % 100 == 0 :
        loss_v = sess.run(loss, feed_dict={
                                 X1:x1_data, 
                                 X2:x2_data, 
                                 Y:y_data})
        print(f"{step} : {loss_v}")
        
    if loss_v1 != None and (loss_v1 < loss_v2 or loss_v1 == loss_v2) :
        break
    else:
        loss_v1 = loss_v2
        step += 1        

h_v = sess.run(H, feed_dict={X1:[10], X2:[13]})
print(h_v)
from matplotlib import pyplot as plt
plt.title("Loss Trend")
plt.xlabel("Count")
plt.ylabel("Loss Data")
plt.plot([i for i in range(1, step+1)], loss_list, "r--")
plt.show()














