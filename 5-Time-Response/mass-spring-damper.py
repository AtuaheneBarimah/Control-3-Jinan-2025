import control
import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 5.0       # Mass (kg)
c = 1.0       # Damping coefficient (N·s/m)
k = 10.0      # Spring stiffness (N/m)

# Transfer function: X(s)/F(s) = (k+c*s) / (m*s² + c*s + k)
s = control.TransferFunction.s
sys = (k+c*s)/((m*s**2)+c*s+k)
print("Transfer Function =", sys)

#Controller
Kp = 0.4
Ti = 0.01
num = np.array ([Kp*Ti, Kp])
den = np.array ([Ti , 0])
Hc = 10
#Hc = control.tf(num , den)

#Series connection of controller and system
sys = control.series(Hc, sys)
sys = control.feedback(sys, 1)

# Step response
time = np.linspace(0, 50, 1000)
t, y = control.step_response(sys, time)

# Step input (reference signal)
step_input = np.ones_like(t)

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

print("\nTime-Domain Characteristics:")
print(f"Natural Frequency (ωₙ) = {omega_n:.2f} rad/s")
print(f"Damping Ratio (ζ) = {zeta:.3f}")
print(f"Rise Time (10%-90%) = {rise_time:.3f} s")
print(f"Peak Time = {peak_time:.3f} s")
print(f"Maximum Overshoot = {max_overshoot:.2f}%")
print(f"Settling Time (2%) = {settling_time:.3f} s")

# Plotting
plt.figure(figsize=(10, 6))
#plt.plot(t, step_input, 'b', linewidth=2, label="Step Input")
plt.plot(t, y, linewidth=2, label="Step Response")
plt.axhline(steady_state, color='r', linestyle='--', label="Steady-State")
plt.axhline(1.02 * steady_state, color='g', linestyle=':', label="±2% Tolerance")
plt.axhline(0.98 * steady_state, color='g', linestyle=':')
plt.scatter(peak_time, np.max(y), color='k', label=f"Peak Overshoot: {max_overshoot:.1f}%")
plt.title("Mass-Spring-Damper Step Response")
plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t)")
plt.grid()
plt.legend()
plt.show()