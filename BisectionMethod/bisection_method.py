#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bis(x):
    return x**3-2*x-5


# In[2]:


r1 = 2
f1 = bis(r1)


# In[3]:


r2 = 3
f2 = bis(r2)


# In[4]:


for i in range(50):
    
    r1 = round(r1,5)
    r2 = round(r2,5)
    
    print("root1 : ",r1)
    print("root2 : ",r2)
    
    a = (r1+r2)/2
    b = bis(a)
    
    print("average : ",a)
    print("average function value : ",b)
    
    if (b<0) and (b>f1):
        r1=a
        
    if (b>=0) and (b<f2):
        r2=a
        
    if (r1==r2):
        print("we find the exact root")
        break
print("Final root : ",r1)

# In[ ]:




