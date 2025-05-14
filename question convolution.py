#convolution Determine the output  y(n) = x(n)*h(n) using the convolution sum.

import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def unit_step(n):
  return np.array([1 if i >= 0 else 0 for i in n])

n = np.arange(0, 11)
x = unit_step(n)      #define x[n]=u(n)
h = unit_step(n) - unit_step(n-5)

y = np.convolve(x, h)
n_y = np.arange(0, len(y))
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt=" ")
plt.title("Input x[n] = u(n)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h, basefmt=" ")
plt.title("Impulse Response h[n] = u(n) - u(n-5)")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n_y, y)
plt.title("Output y[n] = x[n] * h[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)

plt.tight_layout()
plt.show()