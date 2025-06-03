import control
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# System parameters
m = 1.0       # Mass (kg)
c = 0.5       # Damping coefficient (N·s/m)
k = 1.0      # Spring stiffness (N/m)

# Simulation parameters
sim_time = 50  # Total simulation time in seconds
time_vector = np.linspace(0, sim_time, 5000)  # Increased resolution

# Create the transfer function
s = control.TransferFunction.s
sys = (k + c*s)/(m*s**2 + c*s + k)
print("Transfer Function =", sys)

# Improved closed-loop identification with better oscillation detection
def ziegler_nichols_cl_identification(sys, time_vector, max_Kp=1000):
    Kp = 0.1
    Ku = 0
    Tu = 0
    best_oscillation = (0, 0, 0)  # (Kp, amplitude, n_peaks)
    
    while Kp < max_Kp:
        closed_loop = control.feedback(Kp * sys, 1)
        t, y = control.step_response(closed_loop, time_vector)
        
        # Improved peak detection with minimum height and distance
        peaks, properties = find_peaks(y, height=0.1, distance=20)
        n_peaks = len(peaks)
        
        # Track the best oscillation pattern found
        if n_peaks >= 3:
            avg_amplitude = np.mean(properties['peak_heights'])
            if avg_amplitude > best_oscillation[1]:
                best_oscillation = (Kp, avg_amplitude, n_peaks)
            
        # Check for sustained oscillations (at least 3 full periods)
        if n_peaks >= 4:
            peak_times = t[peaks]
            periods = np.diff(peak_times)
            if np.std(periods)/np.mean(periods) < 0.2:  # Check period consistency
                Ku = Kp
                Tu = np.mean(periods)
                return Ku, Tu
        
        Kp += 0.5 if Kp < 10 else 5  # Adaptive gain increment
    
    # If no perfect oscillation found, use the best candidate
    if best_oscillation[2] >= 3:
        Kp_temp = best_oscillation[0]
        closed_loop = control.feedback(Kp_temp * sys, 1)
        t, y = control.step_response(closed_loop, time_vector)
        peaks, _ = find_peaks(y, height=0.1, distance=20)
        peak_times = t[peaks]
        Tu = np.mean(np.diff(peak_times))
        return Kp_temp, Tu
    
    raise ValueError(f"No sustained oscillations found with Kp < {max_Kp}")

try:
    # Find critical gain and period
    Ku, Tu = ziegler_nichols_cl_identification(sys, time_vector)
    print(f"\nCritical gain Ku = {Ku:.2f}")
    print(f"Critical period Tu = {Tu:.2f} seconds")
    
    # Ziegler-Nichols PID tuning rules
    Kp = 0.6 * Ku
    Ti = 0.5 * Tu
    Td = 0.125 * Tu
    
    # Create PID controller
    pid = Kp * (1 + 1/(Ti * s) + (Td * s))
    
    print("\nPID Controller Parameters:")
    print(f"Kp = {Kp:.4f}")
    print(f"Ti = {Ti:.4f} sec")
    print(f"Td = {Td:.4f} sec")
    #print(f"Derivative filter coefficient N = {N}")
    
    # Create closed-loop system
    closed_loop_pid = control.feedback(pid * sys, 1)
    
    # System analysis
    print("\nSystem Analysis:")
    print("Original System Poles:", sys.poles())
    print("Closed-loop Poles:", closed_loop_pid.poles())
    
    # Time response analysis
    t_pid, y_pid = control.step_response(closed_loop_pid, time_vector)
    t_orig, y_orig = control.step_response(sys, time_vector)

    step_input = np.ones_like(t_pid)

    # Calculate Time-domain characteristics
    print("\nTime-Domain Characteristics:")
    info = control.step_info(closed_loop_pid, T=time_vector)
    steady_state = y_pid[-1]
    peak_idx = np.argmax(y_pid)
    peak_time = t_pid[peak_idx]
    max_overshoot = (y_pid[peak_idx] - steady_state)/steady_state * 100
    
    print("\nPerformance Metrics:")
    for key, value in info.items():
        print(f"{key:20s}: {value:.4f}")
    
    # Plotting
    plt.figure(figsize=(12, 8))
    
    # Step response comparison
    plt.plot(t_pid, step_input, 'b', linewidth=2, label="Step Input")
    plt.plot(t_orig, y_orig, label='Open-loop')
    plt.plot(t_pid, y_pid, label='PID-controlled')
    plt.title('Step Response Comparison')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Pole-zero plot
    pzmap = control.pzmap(closed_loop_pid, plot=True, grid=True)
    plt.title('Pole-Zero Map of Closed-Loop System')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"\nError: {str(e)}")
    print("Try adjusting system parameters or simulation time.")