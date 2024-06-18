import numpy as np
a1 = 20 * 3.14/180
a2 = 210 * 3.14/180
da = a2 - a1
th1 = np.arctan2(np.sin(da), np.cos(da)) 
print(th1*180/3.14)