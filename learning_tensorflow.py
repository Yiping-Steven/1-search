#!/usr/bin/python
# coding=utf-8
#定义一个基本函数运算函数，实现加法运算
import tensorflow as tf

def basic_operation():
	v1=tf.Variable(10)
	v2=tf.Variable(5)
	s=v1+v2
	print(s)

#session是用来计算的实例，我们需要先定义一个session，将它初始化，再进行赋值，如下：
sess = tf.Session()
tf.global_variables_initializer().run(session=sess)
#进行初始化
print('变量初始化')
print('v1+v2=',s.eval(session=sess))#打印输出，s.eval()用来计算括号里的session，也可以用.run()实现