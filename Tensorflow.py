import tensorflow as tf
import matplotlib.pyplot as plt

X = [0, 0.5, 1.0, 1.5, 2.0, 2.5]
Y = [0.3, 1.9, 2.4, 4.1, 6.8, 7.9]

w = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random.uniform([1], -1.0, 1.0))

optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.1)

@tf.function()
def cost_eval() :
  hypothesis = w * x + b
  cost = tf.reduce_mean(tf.square(hypothesis - y))
  return cost

print("epoch W  b cost")

for epoch in range(10) :
  optimizer.minimize(cost_eval, var_list=[w, b])
  print(epoch, w.numpy(), b.numpy(), cost_eval().numpy())

print("\n=== Test ===")
x = 5
print('X: ', X, 'Y: ', (w * X + b).numpy())
x = 2.5
print('X: ', X, 'Y: ', (w * X + b).numpy())

new_X = tf.range(0, 3, 0.05)
new_Y = w * new_X + b

plt.plot(X, Y, 'ro', label='Sample Data')
plt.plot(new_X, new_Y, 'b-')
plt.xlabel('X')
plt.xlabel('Y')
plt.legend()
plt.show()