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

car  = 10
reference_signal = r 
disturbance_constant = 0.5
disturbance_signal = 10
disturbance = disturbance_constant*disturbance_signal
output_signal = reference_signal*car

control_signal = 0.1
output_signal_2 = car*((reference_signal*control_signal)-(disturbance))

plt.figure(figsize=(7, 7))
plt.plot(reference_signal, 'b--', label='reference_signal', linewidth=3)
plt.plot(output_signal_2, 'g--', label='output_signal (Disturbance)', linewidth=3)
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.title('With Disturbance')
plt.legend()
plt.grid(True)
plt.show()

error_signal = ((output_signal_2-reference_signal)/reference_signal)*100  # Percentage error
plt.figure(figsize=(7, 7))
plt.plot(error_signal, 'r--', label='error_signal', linewidth=3)
plt.ylabel('Error (%)')
plt.xlabel('Time (s)')
plt.title('Error Signal')
plt.legend()
plt.grid(True)
plt.show()