import control
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

s = control.TransferFunction.s

K = 1000

G = (2*s+1)/((3*s**2)-s-2)

G = control.series(K, G)

print ('H(s) =', G)
G = control.feedback(G,1)
print ('G(s) =', G)
ref = 55
time = 20

t, y = (control.step_response(ref*G,time))
plt.plot(t,y,label='Second Order System', linewidth=3)
plt.title("Step Response")
plt.grid()
plt.show()
