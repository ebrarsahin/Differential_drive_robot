from math import sin,cos

import pylab as plt

import numpy as np

R = 0.05 #wheel radius

L = 0.3 #base length

dt = 0.1 #delta t

def straight_motion(xc,yc,qc,radius,length,dt,wr,wl):

    xn = xc + (R*dt/2.0)*(wr+wl)*cos(qc)
    
    yn = yc + (R*dt/2.0)*(wr+wl)*sin(qc)
    
    qn= 0
    
    return (xn,yn,qn)

def rotation_matrix(xc,yc,qc,r,R,L,dt,wr,wl):

    
    xn= cos(((R*dt/L)*(wr-wl)))* (r*sin(qc)) - sin(((R*dt/L)*(wr-wl)))* (-r*cos(qc)) +( xc-r*sin(qc))
    yn= sin(((R*dt/L)*(wr-wl)))* (r*sin(qc)) + cos(((R*dt/L)*(wr-wl)))* (-r*cos(qc)) + (yc+r*cos(qc))
    qn = qc+ ((R*dt/L)*(wr-wl))
    return (xn,yn,qn)

xc = 0; yc = 0; qc = 0 #x current ,y current q current

print("inital positon arg:",xc,yc,qc)

t = 0

while(t<10):

    w1=10
    
    w2=10
    
    xc, yc, qc = straight_motion(xc,yc,qc,R,L,dt,w1,w2)
    
    t = t + dt

print (int(t),".sn",round(xc,2), round(yc,2),round(qc,2))

while(t>=10 and t<15):
    
    w1=5
    
    w2=10
    
    r=((R / 2.0) * (w1 + w2)) / ((R/(2.0*L))*(w1-w2))
    
    xc, yc, qc = rotation_matrix(xc,yc,qc,r,R,L,dt,w1,w2)
    
    t = t + dt
    
print (int(t),".sn",round(xc,2), round(yc,2),round(qc,2))

while(t>=15 and t<20):

    w1=10
    
    w2=-10
    
    r=0
    
    xc, yc, qc = rotation_matrix(xc, yc, qc,r,R,L,dt,w1,w2)
    
    t = t + dt

print (int(t),".sn",round(xc,1), round(yc,2), round(qc,2))

while(t>=20 and t<25):

    w1=0
    
    w2=10
    
    r=L/2
    
    xc, yc, qc = rotation_matrix(xc, yc,qc,r,R,L,dt,w1,w2)
    
    t = t + dt

print (int(t),".sn",round(xc,2), round(yc,2), round(qc,2))

N=251

x = np.zeros(N)

y = np.zeros(N)

q = np.zeros(N)

x[0] = 0; y[0] = 0; q[0] = 0

t = 0;

for i in range(N-1):

    if t<10:
    
        w1 = 10
        
        w2 = 10
        
        x[i+1], y[i+1], q[i+1] = straight_motion(x[i], y[i], q[i],R,L,dt,w1,w2)
        
    elif t>=10 and t<15:
    
        w1 = 5
        
        w2 = 10
        
        r=((R / 2.0) * (w1 + w2))/((R/(2.0*L))*(w1-w2))
        
        x[i+1], y[i+1], q[i+1] = rotation_matrix(x[i], y[i], q[i],r,R,L,dt,w1,w2)
        
    elif t>=15 and t<20:
    
        w1 = 10
        
        w2 = -10
        
        r=((R / 2.0) * (w1 + w2))/((R/(2.0*L))*(w1-w2))
        
        x[i+1], y[i+1], q[i+1] = rotation_matrix(x[i], y[i], q[i],r,R,L,dt,w1,w2)
        
    elif t>=20 and t<25:
    
        w1=0
        
        w2=10
        
        r=((R / 2.0) * (w1 + w2))/((R/(2.0*L))*(w1-w2))
        
        x[i+1], y[i+1], q[i+1] = rotation_matrix(x[i], y[i], q[i],r,R,L,dt,w1,w2)
        
    t = t + dt

plt.plot(x,y,'rv')

plt.show()   
    
