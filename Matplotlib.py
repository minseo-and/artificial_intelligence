import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

x = [0, 0.5, 1.0, 1.5, 2.0, 2.5]
y = [0.3, 1.9, 2.4, 4.1, 5.8, 7.9]

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)

division = sum((y-y_mean) * (x-x_mean) for y, x in list(zip(y,x)))
divisor = sum((x-x_mean) ** 2 for x in x)
a = division/divisor
b = y_mean * x_mean

new_X = np.arange(0, 3, 0.95)
new_Y = a*new_X+b

print('a:', a, 'b:', b)
plt.plot(x,y, 'ro', label='Sample Data')
plt.plot(new_X, new_Y, 'b-', label='Test Data')
plt.xlabel('X')
plt.xlabel('Y')
plt.legend()
plt.show()
