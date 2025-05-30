import control
import numpy as np
import matplotlib.pyplot as plt

s = control.TransferFunction.s
sys = (3)/((2*s)+1)
print("Transfer Function =", sys)

K = 100

#sys = control.series(K, sys)

G = control.feedback(sys,1)

z = control.zeros(G)
print ('z =', z)
p = control.poles(G)
print ('p =', p)
control.pzmap(G)
plt.grid()
plt.show()
