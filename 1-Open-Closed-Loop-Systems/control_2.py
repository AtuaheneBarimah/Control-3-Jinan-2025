import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

ref = 55
r = ref*(np.ones(100))  # Step input

car  = 10
reference_signal = r 
disturbance = 10
output_signal = reference_signal*car

control_signal = 0.1
output_signal_2 = reference_signal-(5*disturbance)

plt.figure(figsize=(7, 7))
plt.plot(reference_signal, 'b--', label='reference_signal')
plt.plot(output_signal_2, 'g--', label='output_signal (Disturbance)')
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.title('With Disturbance')
plt.legend()
plt.grid(True)
plt.show()