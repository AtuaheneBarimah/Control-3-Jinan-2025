import control
import numpy as np
import matplotlib.pyplot as plt

s = control.TransferFunction.s
sys = (3)/((2*s)+1)
print("Transfer Function =", sys)

K = 100

sys = control.series(K, sys)

sys_1 = control.feedback(sys,1)

time = 50
t, y = (control.step_response(sys_1,time))
plt.plot(t,y,label='Second Order System', linewidth=3)
plt.title("Step Response")
plt.grid()
plt.show()