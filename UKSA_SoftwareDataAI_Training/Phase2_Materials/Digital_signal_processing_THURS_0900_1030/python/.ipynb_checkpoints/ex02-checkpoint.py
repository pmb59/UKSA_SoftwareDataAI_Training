import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sinc
from scipy.signal import hamming, lfilter

# Parameters
f1 = 0.5e3
fs = 10e3
fcf = f1 * 1.1
Omegacf = 2 * np.pi * fcf / fs
M = 101
n = np.arange(0, M) - np.floor(M / 2)
h = Omegacf / np.pi * np.sinc(n * Omegacf / np.pi)
w = hamming(M)
# w = np.ones(M)  # Uncomment this line if you want to use a rectangular window
A = 1
B = h * w

# Filter the signal
y = lfilter(B, A, xn)

# Plotting
plt.plot(t, x, linewidth=3, label='original signal')
plt.plot(t, xn, linewidth=1, label='with noise')
plt.plot(t, y, 'g', linewidth=2, label='filtered')
plt.axis([1/f1*100, 1/f1*110, -4, 4])
plt.xlabel('time, s')
plt.ylabel('amplitude, arbitrary units')
plt.legend()
plt.show()
