#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random


d = 2 # objective function's dimention
n = 100 # number of particles to be generated
w = 0.5 # inertia of the particle 
c1 = 2 
c2 = 2
x = np.zeros((n,d))
# random postion for each particle
for i in range(n):
    for j in range(d):
        x[i][j] = random.uniform(1,100)



# random velocity for each particle
velocity = np.zeros((n,d))

for i in range(n):
    for j in range(d):
        velocity[i][j] = random.uniform(1,100)


# objective function.
def myfunc(x):
    return x[0]**2  + 4*x[0] + x[1]**2 # can be changed for any desired function 

minimum = [-2,0] #should be changed based on the objective function

# the algorithm 
def PSO(func):
    gBest = np.array([float('inf') for i in range(d)])
    pBest =np.zeros((n,d))
    for k in range(100):
        for i in range(n):
            if myfunc(x[i]) < myfunc(pBest[i]):
                pBest[i] = x[i]
        for i in range(n):
            if myfunc(pBest[i]) < myfunc(gBest):
                gBest = pBest[i]
        if abs(myfunc(gBest) - minimum[0] )<0.1 and abs(myfunc(gBest) - minimum[1] )<0.1:
                break
        for i in range(n):
            velocity[i] = (w*velocity[i]) + (c1*random.uniform(0,1))*(pBest[i] - x[i]) + (c2*random.uniform(0,1)) * (gBest[j] - x[i])
            x[i] = x[i] + velocity[i]
    return gBest

print(PSO(myfunc))


# In[ ]:





# In[ ]:




