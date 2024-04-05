from tkinter import*
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

# Creating a GUI window with a title
gui = Tk()
gui.title("SCARA Design Calculator")
gui.resizable(False,False)
gui.config(bg="pink")

def reset():
    a1_E.delete(0, END)
    a2_E.delete(0, END)
    a3_E.delete(0, END)
    a4_E.delete(0, END)
    a5_E.delete(0, END)

    t1_E.delete(0, END)
    t2_E.delete(0, END)
    d3_E.delete(0, END)

    X_E.delete(0, END)
    Y_E.delete(0, END)
    Z_E.delete(0, END)

def f_k():
    #link lengths in mm

    a1 = float(a1_E.get())/100

    a2 = float(a2_E.get())/100

    a3 = float(a3_E.get())/100

    a4 = float(a4_E.get())/100

    a5 = float(a5_E.get())/100

    #joint variables: is mm if f, is degrees if theta

    T1 = float(t1_E.get()) 

    T2 = float(t2_E.get()) 

    D3 = float(d3_E.get())/100

    #degree to radian

    T1 = (T1/180.0)*np.pi

    T2 = (T2/180.0)*np.pi

    #Parametric Table (theta, alpha, r, d)

    PT = [[(0.0/180.0)*np.pi + T1,(0.0/180.0)*np.pi,a2,a1], 
    [(0.0/180.0)*np.pi + T2,(180.0/180.0)*np.pi,a4,a3],
    [(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a5+ D3]]

    #HTM formula and multiplication

    i = 0

    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])], [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
    [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
    [0,0,0,1]]

    i = 1

    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])], [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
    [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
    [0,0,0,1]]

    i = 2

    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])], [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
    [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
    [0,0,0,1]]

    #Multiply the matrices

    H0_1 = np.matrix(H0_1)

    H1_2 = np.matrix(H1_2)

    H2_3 = np.matrix(H2_3)

    H0_2 = np.dot(H0_1,H1_2)
    H0_3 = np.dot(H0_2,H2_3)

    X0_3 = H0_3[0,3]
    X_E.delete(0,END)
    X_E.insert(0,np.around(X0_3*100,3))

    Y0_3 = H0_3[1,3]
    Y_E.delete(0,END)
    Y_E.insert(0,np.around(Y0_3*100,3))

    Z0_3 = H0_3[2,3]
    Z_E.delete(0,END)
    Z_E.insert(0,np.around(Z0_3*100,3))

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

    SCARA.teach (q=(0,0,0,0,0,0))

    # plot scale
    x1 = -0.8
    x2 = 0.8
    y1 = -0.8
    y2 = 0.8
    z1 = 0
    z2 = 0.8

    # Plot command
    SCARA.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

def i_k():
    #link lengths in cm
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())
    a4 = float(a4_E.get())
    a5 = float(a5_E.get())

    #Position Vector in cm
    x0_3 = float(X_E.get())
    y0_3 = float(Y_E.get())
    z0_3 = float(Z_E.get())


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
    th1 = phi2 - phi1

    # solution 5
    phi3 = np.arccos((r1**2-a2**2-a4**2)/(-2*a2*a4))
    phi3 = phi3*180/np.pi

    # Solution 6
    th2 = 180 - phi3

    # Solution 7
    d3 =  a1 + a3 - a5 -z0_3  

    #Multiply the matrices

    t1_E.delete(0,END)
    t1_E.insert(0,np.around(th1,3))

    t2_E.delete(0,END)
    t2_E.insert(0,np.around(th2,3))

    d3_E.delete(0,END)
    d3_E.insert(0,np.around(d3,3))

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
    
    SCARA.teach (q=(0,0,0,0,0,0))

    # plot scale
    x1 = -0.8
    x2 = 0.8
    y1 = -0.8
    y2 = 0.8
    z1 = 0
    z2 = 0.8

    # Plot command
    SCARA.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)




##Frane
FI = LabelFrame(gui,text="Link Lenghts and joint variable", font=(5))
FI.grid(row=0,column=0)

#Link lenghts 
a1 = Label(FI,text=("a1 = "),font=(10))
a1_E = Entry(FI,width=5,font=(10))
cm1 = Label(FI,text="cm",font=(10))

a1.grid(row=0,column=0)
a1_E.grid(row=0,column=1)
cm1.grid(row=0,column=2)

a2 = Label(FI,text=("a2 = "),font=(10))
a2_E = Entry(FI,width=5,font=(10))
cm2 = Label(FI,text="cm",font=(10))

a2.grid(row=1,column=0)
a2_E.grid(row=1,column=1)
cm2.grid(row=1,column=2)

a3 = Label(FI,text=("a3 = "),font=(10))
a3_E = Entry(FI,width=5,font=(10))
cm3 = Label(FI,text="cm",font=(10))

a3.grid(row=2,column=0)
a3_E.grid(row=2,column=1)
cm3.grid(row=2,column=2)

a4 = Label(FI,text=("a4 = "),font=(10))
a4_E = Entry(FI,width=5,font=(10))
cm4 = Label(FI,text="cm",font=(10))

a4.grid(row=3,column=0)
a4_E.grid(row=3,column=1)
cm4.grid(row=3,column=2)

a5 = Label(FI,text=("a5 = "),font=(10))
a5_E = Entry(FI,width=5,font=(10))
cm5 = Label(FI,text="cm",font=(10))

a5.grid(row=4,column=0)
a5_E.grid(row=4,column=1)
cm5.grid(row=4,column=2)

## D

t1 = Label(FI,text=("t1 = "),font=(10))
t1_E = Entry(FI,width=5,font=(10))
deg1 = Label(FI,text="deg",font=(10))

t1.grid(row=0,column=3)
t1_E.grid(row=0,column=4)
deg1.grid(row=0,column=5)

t2 = Label(FI,text=("t2 = "),font=(10))
t2_E = Entry(FI,width=5,font=(10))
deg2 = Label(FI,text="deg",font=(10))

t2.grid(row=1,column=3)
t2_E.grid(row=1,column=4)
deg2.grid(row=1,column=5)

d3 = Label(FI,text=("d3 = "),font=(10))
d3_E = Entry(FI,width=5,font=(10))
cm6 = Label(FI,text="cm",font=(10))

d3.grid(row=2,column=3)
d3_E.grid(row=2,column=4)
cm6.grid(row=2,column=5)

BF = LabelFrame(gui,text="Forward and Inverse Kinematics",font=(5))
BF.grid(row=1,column=0)

#Buttons
FK = Button(BF,text="Forward",font=(10),bg="black",fg="pink",command=f_k)
rst = Button(BF,text="Reset",font=(10),bg="black",fg="pink",command=reset)
IK = Button(BF,text="Inverse",font=(10),bg="black",fg="pink",command=i_k)

FK.grid(row=0,column=0)
rst.grid(row=0,column=1)
IK.grid(row=0,column=2)


PV = LabelFrame(gui,text="Position Vector",font=(5))
PV.grid(row=2,column=0)

X = Label(PV,text=("x = "),font=(10))
X_E = Entry(PV,width=5,font=(10))
cm8 = Label(PV,text="cm",font=(10))

Y = Label(PV,text=("y = "),font=(10))
Y_E = Entry(PV,width=5,font=(10))
cm9 = Label(PV,text="cm",font=(10))

Z = Label(PV,text=("z = "),font=(10))
Z_E = Entry(PV,width=5,font=(10))
cm10 = Label(PV,text="cm",font=(10))

X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm8.grid(row=0,column=2)

Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cm9.grid(row=1,column=2)

Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cm10.grid(row=2,column=2)

# insert image
img = PhotoImage(file= "scara.png")
img = img.subsample(5,5)
PI = Label(gui,image=img)
PI.grid(row=3,column=0)


gui.mainloop()