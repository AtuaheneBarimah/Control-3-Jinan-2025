import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

ref = 55
r = ref*(np.ones(100))  # Step input
plt.plot(r, label='Input Signal', linewidth=4)
plt.grid(True)
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.legend()
plt.show()