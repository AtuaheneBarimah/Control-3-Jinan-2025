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
Ti = 0.2
num = np.array ([Kp*Ti, Kp])
den = np.array ([Ti , 0])
Hc = 10
#Hc = control.tf(num , den)
#Hc = control.tf(num , den)

#Series connection of controller and system
sys = control.series(Hc, sys)
G = control.feedback(sys, 1)

z = control.zeros(G)
print ('z =', z)
p = control.poles(G)
print ('p =', p)
control.pzmap(G)
plt.grid()
plt.show()