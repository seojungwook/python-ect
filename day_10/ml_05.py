# -*- coding: utf-8 -*-

import tensorflow as tf

# 입력 데이터의 개수가 2개 이상인 경우의 행렬 처리방법
x_data = [[1., 5.], [2,6],[3,7],[4,8],[5,9]]
y_data = [35., 55, 77, 89, 100]

X = tf.placeholder(tf.float32, shape=[None,2])
Y = tf.placeholder(tf.float32)

# Y의 테이터의 형태를 1 * 5 -> 5 * 1로 변환하는 코드
Y_reshape = tf.reshape(Y, shape=[-1,1])

W = tf.Variable(tf.random_normal([2,1]))
B = tf.Variable(tf.zeros([1]))

H = tf.matmul(X, W) + B

loss = tf.reduce_mean(tf.square(H - Y_reshape))

train = tf.train.GradientDescentOptimizer(
        learning_rate=0.00001).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_list = []
step = 1
loss_v1 = None
loss_v2 = None
while True :
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    loss_v2 = sess.run(loss, feed_dict={X:x_data, Y:y_data})
    loss_list.append(loss_v2)
    
    if step % 100 == 0 :
        loss_v = sess.run(loss, feed_dict={X:x_data, Y:y_data})
        print(f"{step} : {loss_v}")
        
    if loss_v1 != None and (loss_v1 < loss_v2 or loss_v1 == loss_v2) :
        break
    else:
        loss_v1 = loss_v2
        step += 1        

h_v = sess.run(H, feed_dict={X:[[10, 13]]})
print(h_v)
from matplotlib import pyplot as plt
plt.title("Loss Trend")
plt.xlabel("Count")
plt.ylabel("Loss Data")
plt.plot([i for i in range(1, step+1)], loss_list, "r--")
plt.show()














