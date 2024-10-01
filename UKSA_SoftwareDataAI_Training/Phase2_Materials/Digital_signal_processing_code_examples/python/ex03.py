import numpy as np
import matplotlib.pyplot as plt

# Compute the FFT of the signals
X = np.abs(np.fft.fft(x))
Xn = np.abs(np.fft.fft(xn))
Y = np.abs(np.fft.fft(y))

# Frequency bin
fbin = fs / N
f = np.arange(0, fs, fbin)

# Plotting
plt.plot(f, 20 * np.log10(X), linewidth=3, label='original signal')
plt.plot(f, 20 * np.log10(Xn), linewidth=2, label='with noise')
plt.plot(f, 20 * np.log10(Y), 'g', linewidth=1, label='filtered')

plt.axis([0, fs/2, -260, 100])
plt.xlabel('frequency, Hz')
plt.ylabel('magnitude gain, dB')
plt.legend()
plt.show()
