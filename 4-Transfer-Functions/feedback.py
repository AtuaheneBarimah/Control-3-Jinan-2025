import numpy as np
import control
import matplotlib.pyplot as plt
# Controller
Kp = 0.4
Ti = 2
num = np.array ([Kp*Ti, Kp])
den = np.array ([Ti , 0])
Hc = control.tf(num , den)
# Process
num = np.array ([2])
den = np.array ([3 , 1])
Hp = control.tf(num , den)
L = control.series(Hc, Hp)
print(L)

L = control.feedback(L,1)
print(L)

ref = 1
time = 50
t, y = (control.step_response(ref*L,time))
plt.plot(t,y,label='Second Order System', linewidth=3)
plt.title("Step Response")
plt.grid()
plt.show()