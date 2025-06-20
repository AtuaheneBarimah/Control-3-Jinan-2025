import control
import numpy as np
import matplotlib.pyplot as plt


Input_step = 10
# Simulation parameters
sim_time = 50  # Total simulation time in seconds
time_vector = np.linspace(0, sim_time, 50) 

# Transfer function:
s = control.TransferFunction.s
kh=3.5
o=22

sys = kh/((o*s)+1)
print("OL Transfer Function =", sys)

#PID Controller
Kp = 20
Ti = 1
Td = 10
Hc = (Kp*(1+(1/(Ti*s))+Td*s))

#Series connection of controller and system
sys = control.series(Hc, sys)
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

#Error
Error=((step_input-y)/step_input)*100

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