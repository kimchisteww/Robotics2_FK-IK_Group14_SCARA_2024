import roboticstoolbox as rtb 
import numpy as np 
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

## Create Model
#link lengths in mm
a1 = float(input("a1 ="))
a2 = float(input("a2 ="))
a3 = float(input("a3 ="))
a4 = float(input("a4 ="))
a5 = float(input("a5 ="))


#link conversion to meters
def mm_to_meter(a):
    m = 1000 #1 meter = 1000
    return a/m 

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)
a5 = mm_to_meter(a5)


# limit of variable d1
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)

#Create links
#robot_variable = DHRobot([RevoluteDH(d,r,alpha,offset=theta,qlim)])
#robot_variable = DHRobot([PrismaticDH(d=0,r,alpha,offset=d,qlim)])
SCARA = DHRobot([
   PrismaticDH(0,0,0,0,qlim=[0,0]),
   RevoluteDH(a1,0,(0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    PrismaticDH(0,a2,0,0,qlim=[0,0]),
    RevoluteDH(a3,0,(180/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    PrismaticDH(0,a4,0,0,qlim=[0,0]),
    PrismaticDH(0,(0/180.0)*np.pi,(0/180.0)*np.pi,a5,qlim=[0,0]),
    
], name = "SCARA")

print(SCARA)

SCARA.teach (q=(0,0,0,0,0,0))