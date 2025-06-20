import control
import numpy as np
import math
import matplotlib.pyplot as plt

# Parameters
m = 1.0       # Mass (kg)
c = 1       # Damping coefficient (N·s/m)
k = 1.0      # Spring stiffness (N/m)
R = 1000
C = 10

Input_step = 15
# Simulation parameters
sim_time = 50  # Total simulation time in seconds
time_vector = np.linspace(0, sim_time, 50) 

# Transfer function:
s = control.TransferFunction.s
sys = k/((m*s)+1)
print("OL Transfer Function =", sys)

#Disturbance
Disturbance = 0

#PID Controller
Kp = 1
Ti = 1
Td = 0  
Hc = (Kp*(1+(1/(Ti*s))+Td*s))

#Series connection of controller and system
sys = control.series(Hc-Disturbance, sys)
sys = control.feedback(sys, 1)
print("CL Transfer Function =", sys)

# Pole-zero plot
z = control.zeros(sys)
print ('z =', z)
p = control.poles(sys)
print ('p =', p)
pzmap = control.pzmap(sys, plot=True, grid=True)
plt.title('Pole-Zero Map of Closed-Loop System')
plt.tight_layout()
plt.show()

# Step response
t, y = control.step_response(sys, time_vector)
y = Input_step*y
# Step input (reference signal)
step_input = Input_step*(np.ones_like(t))
# Time-domain characteristics
steady_state = y[-1]
peak_time = t[np.argmax(y)]
max_overshoot = (np.max(y) - steady_state) / steady_state * 100

# Rise time (10% to 90%)
idx_10 = np.argmax(y >= 0.1 * steady_state)
idx_90 = np.argmax(y >= 0.9 * steady_state)
rise_time = t[idx_90] - t[idx_10]

# Settling time (2% tolerance)
settling_idx = np.argmax((np.abs(y - steady_state) <= 0.02 * steady_state) & (t > peak_time))
settling_time = t[settling_idx] if settling_idx > 0 else np.inf

# Natural frequency and damping ratio
omega_n = np.sqrt(k / m)
zeta = c / (2 * np.sqrt(m * k))

#Error
Error=((step_input-y)/step_input)*100

print("\nTime-Domain Characteristics:")
print(f"Natural Frequency (ωₙ) = {omega_n:.2f} rad/s")
print(f"Damping Ratio (ζ) = {zeta:.3f}")
print(f"Rise Time (10%-90%) = {rise_time:.3f} s")
print(f"Peak Time = {peak_time:.3f} s")
print(f"Maximum Overshoot = {max_overshoot:.2f}%")
print(f"Settling Time (2%) = {settling_time:.3f} s")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, step_input, 'b', linewidth=2, label="Step Input")
plt.plot(t, y,'r', linewidth=2, label="Step Response")
plt.title("Air Heater System")
plt.xlabel("Time (s)")
plt.ylabel("Tout [degC]")
plt.grid()
plt.legend()
plt.show()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, Error, 'b', linewidth=2, label="Step Input")
plt.title("PID Controller Error")
plt.xlabel("Time (s)")
plt.ylabel("Error (%)")
plt.grid()
plt.legend()
plt.show()