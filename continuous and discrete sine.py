import numpy as np
import matplotlib.pyplot as plt

# Discrete-time index
n = np.arange(0, 20, 1)   # n = 0 to 19
f = 0.1                   # Frequency in Hz

# Discrete-time signal
x_discrete = np.sin(2 * np.pi * f * n)

# Continuous-time signal
t = np.linspace(0, 19, 1000)  # More points between 0 and 19 for smoothness
x_continuous = np.sin(2 * np.pi * f * t)

# Plot both signals
plt.figure(figsize=(10, 5))
plt.subplot(1,2,1)

# Continuous signal as line
plt.plot(t, x_continuous, label='Continuous-Time Sine', color='blue')

# Discrete signal as stem
#plt.stem(n, x_discrete, basefmt=' ', linefmt='r-', markerfmt='ro', label='Discrete-Time Sine')

# Labels and grid
plt.title('Continuous-Time vs Discrete-Time Sine Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)


plt.subplot(1,2,2)

# Discrete signal as stem
plt.stem(n, x_discrete, basefmt=' ', linefmt='r-', markerfmt='ro', label='Discrete-Time Sine')

# Labels and grid
plt.title('Continuous-Time vs Discrete-Time Sine Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
