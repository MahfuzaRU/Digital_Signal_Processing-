'''
Consider the analog signal: xa(t)=3cos(200πt)+5sin(600πt)+10cos(1200πt). 
Show the effect of sampling rate.  

'''

import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(0,0.02,800)
input_signal = 3*np.cos(200*np.pi*n) + 5*np.sin(600*np.pi*n) + 10*np.cos(1200*np.pi*n)

plt.figure(figsize=(10,6))
plt.subplot(4,1,1)
plt.plot(n, input_signal, label='main signal')
plt.legend()
plt.title('main signal')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

n1=np.arange(0,0.02,1/800)
low_sample = 3*np.cos(200*np.pi*n1) + 5*np.sin(600*np.pi*n1) + 10*np.cos(1200*np.pi*n1)
plt.subplot(4,1,2)
plt.plot(n, input_signal, 'lightgray ',label='main signal')
plt.stem(n1,low_sample, linefmt='r-', markerfmt='ro',label='occur aliasing')
plt.legend()
plt.title('low nyquiest rate')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

n2=np.arange(0,0.02,1/1200)
equal_sample = 3*np.cos(200*np.pi*n2) + 5*np.sin(600*np.pi*n2) + 10*np.cos(1200*np.pi*n2)
plt.subplot(4,1,3)
plt.plot(n, input_signal, 'lightgray',label='main signal')
plt.stem(n2,equal_sample, linefmt='g-', markerfmt='go', label='no occur aliasing')
plt.legend()
plt.title('equal nyquiest rate')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

n3=np.arange(0,0.02,1/2000)
high_sample = 3*np.cos(200*np.pi*n3) + 5*np.sin(600*np.pi*n3) + 10*np.cos(1200*np.pi*n3)
plt.subplot(4,1,4)
plt.plot(n, input_signal,color="lightgray", label='main signal')
plt.stem(n3,high_sample,  linefmt='b-', markerfmt='bo', label='no aliasing')
plt.legend()
plt.title('greater nyquiest rate')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.grid()

plt.tight_layout()
plt.show()