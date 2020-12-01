#!/usr/bin/env python
# coding: utf-8

# # Basic

# In[72]:


a='Aditya'
print(type(a))
a


# In[9]:


del a


# In[10]:


a


# In[11]:


get_ipython().run_line_magic('whos', '')


# In[12]:


x=3
a="aditya"
y=7.3


# In[13]:


get_ipython().run_line_magic('whos', '')


# In[14]:


22/7


# In[15]:


22//7


# In[16]:


10/3


# In[26]:


divmod(10,3)


# In[22]:


if(not(False)):
    print("abcd")
else:
    print("efgh")


# In[29]:


a=input("Enter")


# In[30]:


a


# In[31]:


type(a)


# In[32]:


a=int(a)


# In[33]:


type(a)


# In[36]:


for i in range(2,20,4):
    print(i)


# # Data Structures in Python

# In[44]:


L = [1,2.3,"name",3]
T = (1,2.3,"name",3)
S = {1,2.3,"name",3}
D = {23:"two-three","B":42,"C":"CCD"}


# In[40]:


print(type(L))
print(type(T))
print(type(S))
print(type(D))


# In[45]:


print(L[1])
print(T[1])
print(3 in S)
print(D[23])


# # NUMPY

# In[55]:


import numpy as np
a=np.array([[1,2,3,4,5],[8,7,6,4,5]])
print(a)  


# In[56]:


type(a)


# In[59]:


a.shape


# In[60]:


a.ndim


# In[65]:


b=np.array(3)
b.ndim


# In[70]:


A=np.arange(20,100,3)


# In[71]:


A


# # PANDAS

# In[75]:


import pandas as pd


# In[76]:


print(pd.__version__)


# In[89]:


marks=pd.Series([85,75,65,55], index=['A','B','C','D'])
grads=pd.Series([4.0,3.5,3.0,2.5], index=['A','B','C','D'])


# In[90]:


marks


# In[88]:


marks.values


# In[91]:


grads


# In[92]:


b=pd.DataFrame({'Marks':marks,'Grades':grads})


# In[93]:


b


# In[95]:


b.T
    


# In[96]:


b.values


# In[97]:


b['ScaleMarks']=100*b['Marks']/90


# In[98]:


b


# In[100]:


h=pd.Series(['a','b','c'], index=[1,3,5])


# In[101]:


h[1]


# In[102]:


h[1:3]


# In[103]:


h.loc[1:3]


# In[104]:


h.iloc[1:3]


# In[105]:


b


# In[106]:


b.iloc[2,:]


# In[ ]:




