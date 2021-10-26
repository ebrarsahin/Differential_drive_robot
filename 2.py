from math import sin,cos

import pylab as plt

import numpy as np


R = 0.05 #wheel radius
L = 0.3 #base length
dt = 0.1 #delta t
t= 0    #time initial
[x,y,q]=[0,0,0] #initial position arg
print("initial position: ",[x,y,q])

    
#angular velocity: w=(wr+wl)/2 , w=wr-wl/2L
#linear velocity : V=(wr+wl)*2/R ,
 
class Robot():   
    
    def eulers_method (x,y,q,radius,length,delta_t,wr,wl):
         
        #xn+1= xn+h.f(xn,tn) aproach was used
        
        xnext = x + (R*dt/2.0)*(wr+wl)*cos(q) #this equation is also equal to (VR+VL)*(dt/2) +cos(qc)
        ynext = y + (R*dt/2.0)*(wr+wl)*sin(q) #this equation is also equal to (VR+VL)*(dt/2) +sin(qc)
        qnext=  q + (R*dt/(L))*(wr-wl) # this equation is also equal to (VR-VL)*(dt/L)
        
        return (xnext, ynext, qnext)
    
    while(t<10):
        wr=10
        wl=10
        x, y, q = eulers_method(x, y,q,R,L,dt,wr,wl)
        t = t + dt
    print (int(t),".sn",round(x,2), round(y,2) ,round(q,2))
    while(t>=10 and t<15):
        wr=5
        wl=10
        x, y, q = eulers_method(x, y,q,R,L,dt,wr,wl)
        t = t + dt
    print (int(t),".sn",round(x,2), round(y,2) ,round(q,2))
    
    while(t>=15 and t<20):
        wr=10
        wl=-10
        x, y, q = eulers_method(x, y,q,R,L,dt,wr,wl)
        t = t + dt
    print (int(t),".sn",round(x,2), round(y,2) ,round(q,2))
    
    while(t>=20 and t<25):
        wr=0
        wl=10
        x, y, q = eulers_method(x, y,q,R,L,dt,wr,wl)
        t = t + dt
    print (int(t),".sn",round(x,2), round(y,2) ,round(q,2))
    
    N=251
    x = np.zeros(N)
    y = np.zeros(N)
    q = np.zeros(N)
    x[0] = 0; y[0] = 0; q[0] = 0
    t=0 
    for i in range(N-1):
        if t<10:
            wr = 10
            wl = 10
            x[i+1], y[i+1], q[i+1] = eulers_method(x[i], y[i], q[i],R,L,dt,wr,wl)
        elif t>=10 and t<15:
        
            wr = 5
            wwl = 10  
            x[i+1], y[i+1], q[i+1] = eulers_method(x[i], y[i], q[i],R,L,dt,wr,wl)
        elif t>=15 and t<20:
        
            wr = 10
            wl = -10
            x[i+1], y[i+1], q[i+1] = eulers_method(x[i], y[i], q[i],R,L,dt,wr,wl)
        elif t>=20 and t<25:
        
            wr=0
            wl=10
            x[i+1], y[i+1], q[i+1] = eulers_method(x[i], y[i], q[i],R,L,dt,wr,wl)
        t = t + dt
    
    plt.plot(x,y,'rv')
    plt.show()
