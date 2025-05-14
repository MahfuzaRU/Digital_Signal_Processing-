#question 1: elementary signal generation

#sine : sin(ωn) cos : cos(ωn) unit step : u(n) unit ramp step : nu(n) exponential : a^nu(n)

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)    #fixed random value

n=np.arange(-10, 11, 1)     #range -10 to 10, increment 1
u_n =np.where(n>=0, 1, 0)   #where unit step = 1, if n>=1 else 0

#plot(u,u_n)
plt.stem(n, u_n, label="unit step sequence")
plt.title("unit step sequence")
plt.xlabel("n")
plt.ylabel("u_n")
plt.legend()
plt.grid()
plt.show()

n =  np.arange(-10, 11, 1)
ramp = np.where(n<0, 0, n)

plt.scatter(n, ramp, label="Ramp sequence")
plt.stem(n, ramp)
plt.title("Ramp Sequence")
plt.xlabel("n")
plt.ylabel("r(n)")

plt.legend(loc='best')    #for label position show

plt.grid(True)
plt.show()

A = 1
b = 0.5
t =  np.linspace(0, 10, 50)     #np.linspace(start, stop, num)  (stop)included
y = A * np.exp(b * t)

plt.stem(t, y)
plt.title("Exponential function")
plt.xlabel("Time (1)")
plt.ylabel('y(t)')

plt.grid(True)
plt.show()

#y(t) = A × sin(2πft + φ)
#y(t) = A × cos(2πft + φ)

x = np.linspace(0, 2*np.pi, 1000)     # 1000 points between 0 and 2π
A=4

y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(15,4))      #figure size

plt.subplot(2, 2, 1)
plt.plot(x, y1, color='green', label='Sine Wave')
plt.legend(loc='best')
plt.title("Sive Wave")
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.axhline(y = 0, color='red',)      #horizontal line

plt.grid(True)
plt.show()

plt.subplot(2, 2, 2)
plt.plot(x, y2, color='red', label='Cos Wave')
plt.legend(loc='best')      #label show in position
plt.title("Cos Wave")
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.axhline(color='black',)      #horizontal line, default position y=0
plt.axvline(color='black')       #vertical line
plt.grid(True)
plt.show()