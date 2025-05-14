#You have the analog signal: xa​(t)=3cos(100πt) Now, you are sampling it at two different rates:

#(a) 200 Hz
#(b) 75 Hz

import numpy as np
import matplotlib.pyplot as plt

A = 3
f_analog = 50  # Because 100π = 2πf → f = 50 Hz
t_max = 0.2  # Time duration for visualization

# Sampling rates
fs1 = 200  # Hz
fs2 = 75  # Hz

# Time vectors for sampled signals
n1 = np.arange(0, t_max, 1/fs1)
n2 = np.arange(0, t_max, 1/fs2)

# Sampled signals
x1 = A * np.cos(2 * np.pi * f_analog * n1)  # 200 Hz sampling
x2 = A * np.cos(2 * np.pi * f_analog * n2)  # 75 Hz sampling

plt.figure(figsize=(10, 5))

# 200 Hz plot
plt.subplot(2, 1, 1)
plt.stem(n1, x1, label='Alising')
plt.legend(loc='best')
plt.title("Sampled Signal 200 Hz (No Aliasing)")
plt.xlabel("Time [s]")
plt.ylabel("x[n]")
#plt.axhline(y=0, color='green')
plt.grid(True)

# 75 Hz plot
plt.subplot(2, 1, 2)
plt.stem(n2, x2, label='No Alising')
plt.legend(loc='best')
plt.title("Sampled Signal 75 Hz (Aliasing Occurs)")
plt.xlabel("Time [s]")
plt.ylabel("x[n]")
plt.grid(True)

plt.tight_layout()
plt.show()