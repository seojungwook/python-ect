# -*- coding: utf-8 -*-

# 텐서플로우의 변수 선언
# placeholder : 세션이 실행될 때 전달받는 데이터를 저장하기 위한 변수
# Variable : 특정 값을 가질 수 있는 변수, Variable로 선언된 변수는
#            학습이 진행되는 동안 값을 변경하며 실행됩니다.

import tensorflow as tf

# tf.Variable(초기값)
n1 = tf.Variable(10)
n2 = tf.Variable(7)

r_sum = tf.add(n1, n2)

sess = tf.Session()
# 텐서플로우의 Variable은 아래의 global_variables_initializer
# 함수가 호출되는 시점에 초기화가 진행됩니다.
# 만약 호출하지 않으면 초기화 에러가 발생되어 실행되지 않습니다.
sess.run(tf.global_variables_initializer())

print(sess.run(r_sum))












