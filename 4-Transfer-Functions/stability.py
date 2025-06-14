import control
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

s = control.TransferFunction.s

K = 1000

G = 64/((s**2)+8*s+64)
print ('H(s) =', G)


#G = control.feedback(G,1)
#print ('G(s) =', G)

z = control.zeros(G)
print ('z =', z)
p = control.poles(G)
print ('p =', p)
control.pzmap(G)
plt.grid()
plt.show()