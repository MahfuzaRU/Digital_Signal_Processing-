
import numpy as np
import matplotlib.pyplot as plt

# Time settings
t = np.linspace(0, 1, 1000)  # time from 0 to 1 second, with 1000 samples
f = 15  # frequency in Hz

# Continuous-time signal: sine wave
x = np.sin(2 * np.pi * f * t)

# Plotting
plt.figure(figsize=(8, 4))
plt.plot(t, x, label='x(t) = sin(2πft)')
plt.title('Continuous-Time Sinusoidal Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

