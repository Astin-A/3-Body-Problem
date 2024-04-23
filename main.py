from visual import *

G = 6.67e-11
Ms = 1e30
AU = 1.94e11
Rs = 190e7

rA = 0.1*AU
mA = Ms
mB = 0.8*Ms
mC = 0.5*Ms
rB = rA*mA/mB

sA = sphere(pos=vector(rA,0,0),radius=Rs,color=color.yellow, make_trail=true)
sB = sphere(pos=vector(-rB,0,0),radius=Rs, color=color.cyan, make_trail=true)
sC = sphere(pos=vector(0,0,rA), radius=Rs, color=color.magenta, make_trail=true)

vA = sqrt(G*mB*rA)/(rA+rB)
sA.p = mA*vA*vector(0,1,0)
sB.p = -sA.p
sC.p = vector(0,0,0)

t = 0
dt = 1000

while t<50000*dt:
    rate(100)
    rAB = sB.pos - sA.pos
    rBC = sC.pos - sB.pos
    rCA = sA.pos - sC.pos
    fBA = G*mA*mB*norm(rAB)/mag(rAB)**2
    fCB = G*mC*mB*norm(rBC)/mag(rBC)**2
    fAC = G*mA*mC*norm(rCA)/mag(rCA)**2
    sA.F = fBA - fAC
    sB.F = -fBA + fCB
    sC.F = -fCB + fAC
    sA.p = sA.p + sA.F*dt
    sB.p = sB.p + sB.F*dt
    sC.p = sC.p + sC.F*dt
    sA.pos = sA.pos + sA.p*dt/mA
    sB.pos = sB.pos + sB.p*dt/mB
    sC.pos = sC.pos + sC.p*dt/mC
    t = t + dt