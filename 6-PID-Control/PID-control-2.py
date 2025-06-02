import control
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# System parameters
m = 10.0       # Mass (kg)
c = 0.50       # Damping coefficient (N·s/m)
k = 1.0      # Spring stiffness (N/m)

#Simulation time
Time = 50  # Total simulation time in seconds
# Time vector
Time = np.linspace(0, Time, 1000)

# Create the transfer function
s = control.TransferFunction.s
sys = (k + c*s)/(m*s**2 + c*s + k)
print("Transfer Function =", sys)

# Step 1: Obtain the open-loop step response
t = Time  # Simulation time
t, y = control.step_response(sys, t)

# Step 2: Find the reaction curve parameters (S-shaped curve)
def find_reaction_curve_parameters(t, y):
    # Normalize the response
    y_norm = y/y[-1]
    
    # Find the maximum slope (inflection point)
    dy = np.gradient(y_norm, t)
    max_slope_idx = np.argmax(dy)
    L = t[max_slope_idx]  # Apparent dead time
    T = t[-1] - L         # Time constant
    
    # Draw tangent line at inflection point
    slope = dy[max_slope_idx]
    tangent_line = slope * (t - L)
    
    # Calculate parameters
    K = y[-1]  # Steady-state gain (output/input, input=1 for step)
    R = slope/K  # Reaction rate
    
    return K, L, R, tangent_line

try:
    K, L, R, tangent = find_reaction_curve_parameters(t, y)
    
    print("\nReaction Curve Parameters:")
    print(f"Process gain (K) = {K:.4f}")
    print(f"Apparent dead time (L) = {L:.4f} sec")
    print(f"Reaction rate (R) = {R:.4f} sec^-1")
    
    # Step 3: Apply Ziegler-Nichols open-loop tuning rules
    def ziegler_nichols_open_loop(K, L, R):
        # For PID controller
        Kp = 1.2/(R*L)
        Ti = 2*L
        Td = 0.5*L
        return Kp, Ti, Td
    
    Kp, Ti, Td = ziegler_nichols_open_loop(K, L, R)
    
    print("\nPID Controller Parameters (Ziegler-Nichols Open-Loop):")
    print(f"Kp = {Kp:.4f}")
    print(f"Ti = {Ti:.4f} sec (Integral time)")
    print(f"Td = {Td:.4f} sec (Derivative time)")
    
    # Create PID controller
    pid = Kp * (1 + 1/(Ti * s) + Td * s)
    
    # Create closed-loop system with PID controller
    closed_loop = control.feedback(pid * sys, 1)
    print("\nClosed-Loop Transfer Function with PID Controller:")
    print(closed_loop)
    pzmap = control.pzmap(closed_loop, plot=True, grid=True)
    
    # Simulate the controlled system
    t_cl, y_cl = control.step_response(closed_loop, T=Time)
    print("\nClosed-Loop Step Response Simulation Completed.")

    step_input = np.ones_like(t_cl)

    # Time-domain characteristics
    steady_state = y_cl[-1]
    peak_time = t_cl[np.argmax(y_cl)]
    max_overshoot = (np.max(y_cl) - steady_state) / steady_state * 100

    # Rise time (10% to 90%)
    idx_10 = np.argmax(y_cl >= 0.1 * steady_state)
    idx_90 = np.argmax(y_cl >= 0.9 * steady_state)
    rise_time = t_cl[idx_90] - t_cl[idx_10]

    # Settling time (2% tolerance)
    settling_idx = np.argmax((np.abs(y_cl - steady_state) <= 0.02 * steady_state) & (t_cl > peak_time))
    settling_time = t_cl[settling_idx] if settling_idx > 0 else np.inf

    # Natural frequency and damping ratio
    omega_n = np.sqrt(k / m)
    zeta = c / (2 * np.sqrt(m * k))

    print("\nTime-Domain Characteristics:")
    print(f"Natural Frequency (ωₙ) = {omega_n:.2f} rad/s")
    print(f"Damping Ratio (ζ) = {zeta:.3f}")
    print(f"Rise Time (10%-90%) = {rise_time:.3f} s")
    print(f"Peak Time = {peak_time:.3f} s")
    print(f"Maximum Overshoot = {max_overshoot:.2f}%")
    print(f"Settling Time (2%) = {settling_time:.3f} s")
    
    # Plot results
    plt.figure(figsize=(12, 8))
    
    # Plot open-loop response
    plt.subplot(2, 1, 1)
    plt.plot(t_cl, step_input, 'b', linewidth=2, label="Step Input")
    plt.plot(t, y, label='Open-loop step response')
    plt.plot(t, tangent*y[-1], 'r--', label='Tangent at inflection point')
    plt.axvline(x=L, color='g', linestyle=':', label=f'Dead time L = {L:.2f} sec')
    plt.title('Open-Loop Step Response with Reaction Curve Analysis')
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    
    # Plot closed-loop response
    plt.subplot(2, 1, 2)
    plt.plot(t_cl, y_cl, 'r', label='PID-controlled response')
    plt.title('Closed-Loop Response with Ziegler-Nichols PID')
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error in analysis: {str(e)}")