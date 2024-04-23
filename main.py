from visual import *

G = 6.67e-11
Ms = 1e30
AU = 1.94e11
Rs = 190e7

rA = 0.1*AU
mA = Ms
mB = 0.8*Ms
rB = rA*mA/mB

sA = sphere(pos=vector(rA,0,0),radius=Rs,color=color.yellow)
sB = sphere(pos=vector(-rB,0,0),radius=Rs, color=color.cyan)

vA = sqrt(G*mB*rA)/(rA+rB)
sA.p = mA*vA*vector(0,1,0)
sB.p = -sA.p