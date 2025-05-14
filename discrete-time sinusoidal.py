import numpy as np
import matplotlib.pyplot as plt

n=np.arange(0,10)

#define signals
omega = np.pi / 2
x = np.cos(omega * n)

omega1 = np.pi / 4
x1 = np.cos(omega1 * n)

omega2 = np.pi
x2 = np.cos(omega2 * n)

#plotting
plt.figure(figsize=(8, 6))

plt.subplot(3,1,1)
plt.stem(n, x)
plt.title("x[n] = cos(pi / 2 * n)")
plt.ylim([-1.2, 1,2])
plt.grid(True)

plt.subplot(3,1,2)
plt.stem(n, x1)
plt.title("x[n] = cos(pi / 4 * n)")
plt.ylim([-1.2, 1,2])
plt.grid(True)

plt.subplot(3,1,3)
plt.stem(n, x2)
plt.title("x[n] = cos(pi * n)")
plt.ylim([-1.2, 1,2])
plt.grid(True)

plt.tight_layout()
plt.show()