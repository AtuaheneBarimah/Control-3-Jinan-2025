import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

ref = 1
r = ref*(np.ones(100))  # Step input
#r = np.linspace(ref, ref/ref, 100)  # Step input (Decreasing)
#r = np.linspace(ref/ref, ref, 100)  # Step input (Increasing)
#r = (ref*signal.square(1 * np.pi * 0.1 * np.arange(100)))  # Square wave input
#r = (ref*signal.sawtooth(1 * np.pi * 0.1 * np.arange(100)))  # Sawtooth wave input
#r = (ref*signal.sawtooth(1 * np.pi * 0.1 * np.arange(100), 0.5))  # Triangular wave input
#r = (ref*signal.chirp(np.arange(100), 0, 10, 1))  # Chirp signal input
#r = (ref*np.sin(1 * np.pi * 0.1 * np.arange(100)) + 1)  # Sine wave input

car  = 1
reference_signal = r
db = 0.25
disturbance_signal = (db)*100 # Disturbance signal
disturbance_constant = 1
disturbance_gain = disturbance_constant*car

gain = 100

output_signal_2 = ((car*gain)/(1+ (car*gain))*reference_signal) - ((disturbance_gain*disturbance_signal)/(1+(car*gain)))

plt.figure(figsize=(7, 7))
plt.plot(reference_signal, 'b--', label='reference_signal', linewidth=3)
plt.plot(output_signal_2, 'g--', label='output_signal (Disturbance)', linewidth=3)
plt.ylabel('Output (mph)')
plt.xlabel('Time (s)')
plt.title('Hig Gain feedback With Disturbance')
plt.legend()
plt.grid(True)
plt.show()

error_signal = ((-output_signal_2+reference_signal))*gain
plt.figure(figsize=(7, 7))
plt.plot(error_signal, 'r--', label='Control_signal', linewidth=3)
plt.ylabel('Control signal')
plt.xlabel('Time (s)')
plt.title('Control Signal')
plt.legend()
plt.grid(True)
plt.show()

error_signal = ((-output_signal_2+reference_signal)/reference_signal)*100  # Percentage error
plt.figure(figsize=(7, 7))
plt.plot(error_signal, 'r--', label='Level of Severity', linewidth=3)
plt.ylabel('Level of Severity (%)')
plt.xlabel('Time (s)')
plt.title('Level of Severity')
plt.legend()
plt.grid(True)
plt.show()