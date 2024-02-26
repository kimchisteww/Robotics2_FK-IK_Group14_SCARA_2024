### Inverse Kinematics of SCARA

import numpy as np

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))
a5 = float(input("a5 = "))

# Position Vector in mm
x0_3 = float(input("x0_3 = "))
y0_3 = float(input("y0_3 = "))
z0_3 = float(input("z0_3 = "))

# Inverse Kinematic Solutions using Graphical Method

# Solution 1
phi2 = np.arctan(y0_3/x0_3)
phi2 = phi2*180/np.pi

# Solution 2
r1 = np.sqrt((y0_3**2)+(x0_3**2))

# Solution 3
phi1 = np.arccos((a4**2-r1**2-a2**2)/(-2*r1*a2))
phi1 = phi1*180/np.pi

# Solution 4
theta1 = phi2 - phi1

# solution 5
phi3 = np.arccos((r1**2-a2**2-a4**2)/(-2*a2*a4))
phi3 = phi3*180/np.pi

# Solution 6
theta2 = 180 - phi3

# Solution 7
d3 =  a1 + a3 - a5 -z0_3  

print("theta1 = ", np.around(theta1,3))
print("theta2 = ", np.around(theta2,3))
print("d3 = ", np.around(d3,3))