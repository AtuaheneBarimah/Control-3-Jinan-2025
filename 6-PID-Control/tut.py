import control
import numpy as np
import matplotlib.pyplot as plt


s = control.TransferFunction.s

# Parameters
m = 1.0       # Mass (kg)
c = 0.05       # Damping coefficient (N·s/m)
k = 1.0      # Spring stiffness (N/m)

gain = 5
Input_step = 5

# Simulation parameters
sim_time = 50  # Total simulation time in seconds
time_vector = np.linspace(0, sim_time, 50) 

# Transfer function:

sys = (1)/((s**2)+s+(1))
print("OL Transfer Function =", sys)

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
t, y = (control.step_response(sys, time_vector))
# Step input (reference signal)
Input_step = 5
step_input = Input_step*(np.ones_like(t))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, step_input, 'b', linewidth=2, label="Step Input")
plt.plot(t, Input_step*y, linewidth=2, label="Step Response")
plt.title("Mass-Spring-Damper Step Response")
plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t)")
plt.grid()
plt.legend()
plt.show()