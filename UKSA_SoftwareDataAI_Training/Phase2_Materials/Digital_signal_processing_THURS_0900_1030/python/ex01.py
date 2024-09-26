import numpy as np
import matplotlib.pyplot as plt

# Parameters
f1 = 0.5e3
f2 = 0.6e3
fs = 10e3
Ts = 1 / fs
tlen = 0.5
t = np.arange(0, tlen, Ts)
N = len(t)

# Signals
x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
standev = 1
n = np.random.randn(N) * standev
xn = x + n

# Plotting
plt.plot(t, x, linewidth=3, label='original signal')
plt.plot(t, xn, linewidth=1, label='with noise')
plt.axis([0, 1/f1*10, -4, 4])
plt.xlabel('time, s')
plt.ylabel('amplitude, arbitrary units')
plt.legend()
plt.show()
