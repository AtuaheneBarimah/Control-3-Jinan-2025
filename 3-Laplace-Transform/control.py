import numpy as np
import control
num = np.array ([3])
den = np.array ([2 , 1, 0])
H = control.tf(num , den)
print ('H(s) =', H)