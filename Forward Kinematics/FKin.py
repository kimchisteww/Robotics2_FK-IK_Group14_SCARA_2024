import numpy as np

#link lengths in mm

a1 = float(input("a1 = "))

a2 = float(input("a2 = "))

a3 = float(input("a3 = "))

a4 = float(input("a4 = "))

a5 = float(input("a5 = "))

#joint variables: is mm if f, is degrees if theta

T1 = float(input("T1 = ")) #20 mm

T2 = float(input("T2 = ")) #30 deg

D3 = float(input("D3 = ")) #-90 deg

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

Multiply the matrices

H0_1 = np.matrix(H0_1)

print("H0_1= ")

print(H0_1)

H1_2 = np.matrix(H1_2)

print("H1_2= ")

print(H1_2)

H2_3 = np.matrix(H2_3)

print("H2_3= ")

print(H2_3)

H0_2 = np.dot(H0_1,H1_2)

H0_3 = np.dot(H0_2,H2_3)

print("H0_3= ")

print(np.matrix(np.around(H0_3,3)))