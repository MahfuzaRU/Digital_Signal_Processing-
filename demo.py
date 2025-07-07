'''
Given x(n)=[1,3,−2,4] y(n)=[2,3,−1,3] z(n)=[2,−1,4,−2] 
Find the correlation between x(n) & y(n) and y(n) & z(n). ⟹ observe the 
realization. 
'''


import numpy as np
import matplotlib.pyplot as plt

# Signals
x = np.array([1, 3, -2, 4])
y = np.array([2, 3, -1, 3])
z = np.array([2, -1, 4, -2])

# Normalized Correlation function
def correlation(a, b):      #any two variable like x,y
    numerator = np.sum(a * b)
    denominator = np.sqrt(np.sum(a ** 2)) * np.sqrt(np.sum(b ** 2))
    return numerator / denominator

# Cross-correlation with lag
def Cal_correlation(a, b):    #any two variable like x,y
    N = len(a) + len(b) - 1
    result = np.zeros(N)
    for i in range(N):
        sum = 0
        for k in range(len(a)):
            if i - k >= 0 and i - k < len(b):
                sum += a[k] * b[i - k]
        result[i] = sum
    return result

# Normalized correlation values
r_xy = correlation(x, y)
r_yz = correlation(y, z)

# Cross-correlation values with reversed second signal
r_xy_0 = Cal_correlation(x, y[::-1])
r_yz_0 = Cal_correlation(y, z[::-1])

# Lag range
lag = np.arange(-len(x) + 1, len(y))

# Plotting
plt.figure(figsize=(10, 6))

# subplot 1: correlation between x and y
plt.subplot(2, 1, 1)
plt.title('Cross-Correlation between x(n) and y(n)')
plt.stem(lag, r_xy_0, linefmt='b-', markerfmt='bo', basefmt='k-', label=f'r_xy = {r_xy:.3f}')
plt.xlabel('Lag')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# subplot 2: correlation between y and z
plt.subplot(2, 1, 2)
plt.title('Cross-Correlation between y(n) and z(n)')
plt.stem(lag, r_yz_0, linefmt='g-', markerfmt='go', basefmt='k-', label=f'r_yz = {r_yz:.3f}')
plt.xlabel('Lag')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

