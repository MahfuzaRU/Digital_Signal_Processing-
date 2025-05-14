import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, -2, 4])
y =  np.array([2, 3, -1, 3])
z = np.array([2, -1, 4, -2])

r_xy = np.correlate(x, y, mode='full')
r_yz = np.correlate(y, z, mode='full')

lags = np.arange(-len(x)+1, len(x))   # same for all three (length 4)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.stem(lags, r_xy, basefmt =" ", label='cross crrelation')
plt.legend(loc='best')
plt.title("Cross Correlation : x(n)*y(n)")
plt.xlabel('lag')
plt.ylabel('correlation')
plt.axhline(color='red')
plt.axvline(color='red')
plt.grid(True)


plt.subplot(1, 2, 2)
plt.stem(lags, r_yz, basefmt =" ", label='cross crrelation')
plt.legend(loc='best')
plt.title("Cross Correlation : x(n)*z(n)")
plt.xlabel('lag')
plt.ylabel('correlation')
plt.axhline(color='red')
plt.axvline(color='red')
plt.grid(True)

plt.tight_layout()  #automatic adjust label, title, axis
plt.show()
