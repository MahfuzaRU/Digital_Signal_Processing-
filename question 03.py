#To show that the highest rate of oscillation in a discrete-time sinusoid occurs when ω=π, let's analyze the behavior of the signal:


import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11, 1)

#frequencies
omega1 = 0.5*np.pi
omega2 = np.pi

#signals
x1 = np.cos(omega1 * n)
x2 = np.cos(omega2 * n)

plt.figure(figsize=(10, 4))

# ω = 0.5π
plt.subplot(1, 2, 1)
plt.stem(n, x1,label='low Ossillation at w=0.5*pi')
plt.legend(loc='best')
plt.title('ω = 0.5*pi')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)


# ω = π
plt.subplot(1, 2, 2)
plt.stem(n, x2,label='high Ossillation at w=pi')
plt.legend(loc='upper right')
plt.title('ω = pi')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
