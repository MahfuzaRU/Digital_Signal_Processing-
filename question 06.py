'''
 The impulse response of a discrete-time LTI system is h(n)={u(n)−u(n−5)}. 
Determine the output of the system for the input x[n]=u(n), using the convolution 
sum. 
 discrete-time Linear Time-Invariant (LTI) system:


      ∞
y[n]= ∑=x[k]⋅h[n−k]
     k=−∞
'''

import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    return np.where(n>=0, 1, 0)
def impluse_h(n):
    return unit_step(n) - unit_step(n-5)
def x(n):
    return unit_step(n)

n=np.arange(0,15,1)
h = unit_step(n) - unit_step(n-5)
x = unit_step(n)

plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.stem(n,x)
plt.title('Input Signal x[n] = u(n)')
plt.xlabel('n (discrete time)')
plt.ylabel('x[n]')
plt.grid()

plt.subplot(3,1,2)
plt.stem(n,h)
plt.title('Impulse Response h[n] = u(n) - u(n−5)')
plt.xlabel('n (discrete time)')
plt.ylabel('h[n]')
plt.grid()

y=np.zeros(len(n))

for i in range(len(n)):
    sum = 0
    for k in range(len(n)):
        if i-k>=0:
            sum += x[k]*h[i-k]
    y[i]=sum
    

plt.subplot(3,1,3)
plt.stem(n,y)
plt.title('convolution sum')
plt.xlabel('n (discrete time)')
plt.ylabel('y(n)')
plt.grid()

plt.tight_layout()
plt.show()