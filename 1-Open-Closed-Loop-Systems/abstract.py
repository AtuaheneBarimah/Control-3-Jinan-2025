import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

ref = 55
r = ref*(np.ones(100))  # Step input

car  = 500
reference_signal = r 
disturbance_signal = 500
disturbance_gain = 0.5*car

gain = 1

output_signal_2 = ((car*gain)/(1+ (car*gain))*reference_signal) - ((disturbance_gain*disturbance_signal)/(1+(car*gain)))

plt.figure(figsize=(7, 7))
plt.plot(reference_signal, 'b--', label='reference_signal')
plt.plot(output_signal_2, 'g--', label='output_signal (Disturbance)')
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.title('Hig Gain feedback With Disturbance')
plt.legend()
plt.grid(True)
plt.show()