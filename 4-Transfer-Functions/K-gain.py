import numpy as np
import control
import matplotlib.pyplot as plt
T = 10
Karray = [1, 3, 5, 10]
start = 0
stop = 60
step = 0.1
t = np.arange(start, stop, step)
for K in Karray:
#Create Transfer Function
    num = np.array ([K])
    den = np.array ([T , 1])
    H = control.tf(num , den)
    print ('H(s) =', H)
    # Step Response
    t, y = control.step_response(H, t)
# Plot
plt.plot(t, y)
plt.title("Step Response for different K")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(Karray)
plt.grid()
plt.show()