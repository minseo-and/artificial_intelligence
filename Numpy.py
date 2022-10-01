import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = [1,2,3]
w = tf.Variable(tf.random.normal([1], dtype = tf.float32))
b = tf.Variable(tf.random.normal([1], dtype = tf.float32))

y = x * w + b#forward(x)

print(y)