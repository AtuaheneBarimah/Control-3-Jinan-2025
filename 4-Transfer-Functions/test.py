import control
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

s = control.TransferFunction.s

Kp = 100
Ti = 0.001
# Controller
Hc = Kp

G = 1/(s + 1) 

H = control.series(Hc, G)
print('H(s) =', H)
L = control.feedback(H, 1)
print('L(s) =', L)

ref = 1
time = 20

t, y = (control.step_response(ref*L,time))
plt.plot(t,y,label='Second Order System', linewidth=3)
plt.title("Step Response")
plt.grid()
plt.show()