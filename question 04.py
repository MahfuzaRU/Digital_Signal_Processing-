'''
Consider the continuous-time analog signal x(t)=3cos(100πt). Sample the analog 
signal at 200 Hz and 75 Hz. Show the discrete-time signal after sampling. ⟹
realization
'''
import numpy as np
import matplotlib.pyplot as plt

def ax(t):
    return 3 * np.cos(100 * np.pi * t)  # 50 Hz cosine signal

n=np.linspace(0, 0.1, 1000)
y = 3*np.cos(100*np.pi*n)

plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.plot(n, y, label = 'input signal')
plt.legend()
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

n1=np.arange(0,0.1, 1/75)
y1=3*np.cos(100*np.pi* n1)
plt.subplot(3,1,2)
plt.plot(n, y, label = 'input signal')
plt.stem(n1,y1, 'g', label='sampled for 75 hz')
plt.legend()
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

n2=np.arange(0,0.1, 1/200)
y2=3*np.cos(100*np.pi* n2)
plt.subplot(3,1,3)
plt.plot(n, y, label = 'input signal')
plt.stem(n2,y2, 'r', label='sampled for 200 hz')
plt.legend()
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

plt.tight_layout()
plt.show()
