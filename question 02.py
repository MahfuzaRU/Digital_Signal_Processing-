#emonstrates the effect of sampling, aliasing

import numpy as np
import matplotlib.pyplot as plt
t_cont = np.linspace(0,1,1000)
fs = 5
y_cont = np.sin(2*np.pi*fs*t_cont)

# f1=20 HZ (not aliasing)
f1 = 20
t1 = np.linspace(0,1,f1)
y1 = np.sin(2*np.pi*fs*t1)

# f2 = 10 Hz Nyquist signal
f2 = 10
t2 = np.linspace(0,1,f2)
y2 = np.sin(2*np.pi*fs*t2)

#f3 = 6 Hz Aliasing Signal
f3 = 6
t3 = np.linspace(0,1,f3)
y3 = np.sin(2*np.pi*fs*t3)

plt.subplot(2,2,1)
plt.plot(t_cont,y_cont)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Main Signal")
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(t_cont, y_cont, color='lightgray', label='Original')
plt.stem(t1, y1, basefmt=" ", linefmt="g", markerfmt="go")
plt.xlabel("Time")
plt.title("Non Aliased")
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(t_cont,y_cont, label="original", color="lightgray")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Nyquist rate")
plt.stem(t2,y2,basefmt=" ",linefmt="r", markerfmt="ro")
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(t_cont,y_cont, label="original", color="lightgray")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Aliased")
plt.stem(t3,y3,basefmt=" ",linefmt="b", markerfmt="ro")
plt.grid(True)
plt.tight_layout()
plt.show()

