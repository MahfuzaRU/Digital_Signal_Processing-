'''
Filter realization using 6-point averaging, 6-point differencing equations. 
'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(40)
n = np.linspace(0, 1, 200)
x = np.sin(2*np.pi*5*n) + 0.5*np.random.randn(len(n))

def avg_filter(x):
    y = np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = np.sum(x[i-5:i+1])/6
    return y

def diff_filter(x):
    y=np.zeros_like(x)
    for i in range(5, len(x)):
        y[i] = (x[i] - x[i-1] + x[i-2] - x[i-3] + x[i-4] - x[i-5])/6
    return y


y_avg = avg_filter(x)
y_diff = diff_filter(x)

plt.figure(figsize=(10, 6))

plt.subplot(3,1,1)
plt.plot(n,x, 'gray')
plt.title('Original Analog-like Signal (with Noise)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3,1,2)
plt.plot(n,y_avg, 'g')
plt.title('Filtered Signal using 6-Point Averaging Filter (Low-pass)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(3,1,3)
plt.plot(n,y_diff, 'r')
plt.title('Filtered Signal using 6-Point differencing Filter (High-pass)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show( )