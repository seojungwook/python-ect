# -*- coding: utf-8 -*-

import tensorflow as tf

# 변수의 생성
# placeholder 타입의 변수는 텐서플로우 세션이 실행될 때
# 값을 전달받는 변수
# 학습데이터 또는 라벨데이터를 전달받는 목적으로 사용
n1 = tf.placeholder(dtype=tf.float32, shape=[1], name="n1")
n2 = tf.placeholder(dtype=tf.float32, shape=[1], name="n1")

result_sum = tf.add(n1, n2)
result_sub = tf.subtract(n1, n2)
result_mul = tf.multiply(n1, n2)
result_div = tf.divide(n1, n2)

#print(n1)
#print(result_sum)

sess = tf.Session()
sum_v = sess.run(result_sum, feed_dict={n1:[10], n2:[5]})
print(sum_v)
sub_v = sess.run(result_sub, feed_dict={n1:[10], n2:[5]})
print(sub_v)
mul_v = sess.run(result_mul, feed_dict={n1:[10], n2:[5]})
print(mul_v)
div_v = sess.run(result_div, feed_dict={n1:[10], n2:[5]})
print(div_v)









