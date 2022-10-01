import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.0, 2.0, 0.1)

y1 = x
y2 = x**2
y3 = x**3

plt.figure(3, figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(x, y1, 'ro-')
plt.subplot(1, 3, 2)
plt.plot(x, y2, 'bs--')
plt.subplot(1, 3, 3)
plt.plot(x, y3, 'g^:')
plt.show()