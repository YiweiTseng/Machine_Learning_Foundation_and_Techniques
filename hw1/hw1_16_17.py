#!/usr/bin/env python
# coding: utf-8

# In[255]:


import pandas as pd
import numpy as np
import random as rdm
from statistics import median


# In[256]:


mydata = pd.read_csv("https://www.csie.ntu.edu.tw/~htlin/course/ml20fall/hw1/hw1_train.dat" , sep="\s+", header = None)


# In[257]:


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


# In[265]:


N = 100
data = mydata.to_numpy()
x = np.ones([N,11])
ans_y = np.empty(N)
for i in range(N):
    ans_y[i] = data[i,10]
    for j in range(10):
        x[i,j+1] = data[i,j]


# In[266]:


times = 1000
updates= np.empty(times)
w0 = np.empty(times)

for i in range(times):
    w = np.zeros(11)
    correct_counter = 0
    updates_counter = 0
    while(correct_counter < 5 * N):
        t = rdm.randint(0,N - 1)
        xt = x[t,:]
        wx = np.inner(w,xt)
        if sign(wx) != ans_y[t]:
            w = w + ans_y[t] * xt
            correct_counter = 0
            updates_counter += 1
        else:
            correct_counter += 1
    
    wPLA = w
    updates[i] = updates_counter
    w0[i] = wPLA[0]
    
ans_16 = median(updates)
ans_17 = median(w0)
print("The median number of updates =", ans_16)
print("The median number of wPLA0 =", ans_17)


# In[ ]:




