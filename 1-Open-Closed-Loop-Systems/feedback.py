import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

ref = 55
r = ref*(np.ones(100))  # Step input

car  = 100
reference_signal = r 
disturbance = 10

output_signal_2 = ((1000/1001)*reference_signal)-(5*disturbance*(1/1001))

plt.figure(figsize=(7, 7))
plt.plot(reference_signal, 'b--', label='reference_signal')
plt.plot(output_signal_2, 'g--', label='output_signal (Disturbance)')
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.title('Hig Gain feedback With Disturbance')
plt.legend()
plt.grid(True)
plt.show()