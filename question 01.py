#question 1: elementary signal generation

#sine : sin(ωn) cos : cos(ωn) unit step : u(n) unit ramp step : nu(n) exponential : a^nu(n)
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # fixed random value

n = np.arange(-10, 11, 1)  # n = -10 to 10
u_n = np.where(n >= 0, 1, 0)  # unit step: u(n)

ramp = np.where(n < 0, 0, n)  # unit ramp: n·u(n)

# Exponential signal
A = 1
b = 0.5
t = np.linspace(0, 10, 50)
exp_y = A * np.exp(b * t)

# Sine and cosine
x = np.linspace(0, 2 * np.pi, 1000)
sine_y = np.sin(x)
cos_y = np.cos(x)

# Create figure and subplots
plt.figure(figsize=(14, 10))

# --- Subplot 1: Unit Step ---
plt.subplot(3, 2, 1)
plt.stem(n, u_n)
plt.title("Unit Step Sequence u(n)")
plt.xlabel("n")
plt.ylabel("u(n)")
plt.grid(True)

# --- Subplot 2: Ramp ---
plt.subplot(3, 2, 2)
plt.stem(n, ramp)
plt.title("Ramp Sequence n·u(n)")
plt.xlabel("n")
plt.ylabel("r(n)")
plt.grid(True)

# --- Subplot 3: Exponential ---
plt.subplot(3, 2, 3)
plt.stem(t, exp_y)
plt.title("Exponential Signal: $A·e^{bt}$")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)

# --- Subplot 4: Sine Wave ---
plt.subplot(3, 2, 4)
plt.plot(x, sine_y, color='green', label='Sine')
#plt.stem(x,sine_y)
plt.axhline(0, color='black')
plt.title("Sine Wave: sin(x)")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# --- Subplot 5: Cosine Wave ---
plt.subplot(3, 2, 5)
plt.plot(x, cos_y, color='red', label='Cosine')
plt.axhline(0, color='black')
plt.axvline(np.pi, color='gray', linestyle='--', label='x=π')
plt.title("Cosine Wave: cos(x)")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Adjust layout
plt.tight_layout()
plt.show()


