import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

ref = 55
#r = ref*(np.ones(100))  # Step input
#r = np.linspace(ref, ref/ref, 100)  # Step input (Decreasing)
r = np.linspace(ref/ref, ref, 100)  # Step input (Increasing)
#r = ref*(signal.square(1 * np.pi * 0.1 * np.arange(100)))  # Square wave input
#r = ref*(signal.sawtooth(1 * np.pi * 0.1 * np.arange(100)))  # Sawtooth wave input
#r = ref*(signal.sawtooth(1 * np.pi * 0.1 * np.arange(100), 0.5))  # Triangular wave input
#r = ref*(signal.chirp(np.arange(100), 0, 10, 1))  # Chirp signal input
#r = ref*(np.sin(1 * np.pi * 0.1 * np.arange(100)) + 1)  # Sine wave input

plt.plot(r, label='Input Signal', linewidth=4)
plt.grid(True)
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.legend()
plt.show()