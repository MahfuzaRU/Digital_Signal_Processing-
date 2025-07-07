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
def correlation(x, y):      #any two variable like a,b
    numerator = np.sum(x * y)
    denominator = np.sqrt(np.sum(x ** 2)) * np.sqrt(np.sum(y ** 2))
    return numerator / denominator

def cal_correlation(x,y):
    N = len(x) + len(y) -1
    result = np.zeros(N)
    
    
    for i in range(N):
        sum = 0
        for k in range(len(x)):
            if i-k >= 0 and i-k<len(y):
                sum += x[k]*y[i-k]
        result[i] = sum
    return result

r_xy = correlation(x,y)
r_yz = correlation(y,z)

# Cross-correlation values with reversed second signal
r_xy_0 = cal_correlation(x,y[::-1])
r_yz_0 = cal_correlation(y,z[::-1])
lag = np.arange(-len(x) + 1, len(y))        #arrange a stop er theke 1 kom hoy tai -3 to +3 hobe

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.title('cross_correlation between x and y')
plt.stem(lag, r_xy_0, linefmt='b-', markerfmt='bo', basefmt=' ', label='corr(xy)')
plt.legend()
plt.xlabel('lag')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2,1,2)
plt.title('cross_correlation between x and y')
plt.stem(lag, r_yz_0, linefmt='g-', markerfmt='go', basefmt=' ', label='corr(yz)')
plt.legend()
plt.xlabel('lag')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
