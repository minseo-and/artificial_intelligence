import numpy as np
import tensorflow as tf

def step_func(x) :
  return (x>=0)*1

x = np.array([[1,1], [1,0], [0,1], [0,0]])

y = np.array([[1], [0], [0], [0]])

w = tf.random.normal([2], 0, 1)

b = 1.0
w0 = 0.5

a = 0.1

for i in range(1000) :
  error_sum = 0
  for j in range(4) :
    output = step_func(np.sum(x[j]*w)+b*w0)
    error = y[j][0] - output
    w = w+x[j]*a*error
    b = b+a*error
    error_sum += error

  if i % 50 == 0 :
    print(i, error_sum)

  for i in range(4) :
    if step_func(np.sum(x[i]*w)+b*w0) > 0.0 :
      output=1.0
    else :
      output=0.0
    print('X: ', x[i], 'Y: ', y[i], 'Output:', step_func(np.sum(x[i]*w)+b*w0), 'result:',
          output)