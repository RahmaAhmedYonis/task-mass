#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import*


# In[2]:


seq =AASequence.fromString("VAKA")


# In[4]:


seq.getMonoWeight()


# In[6]:


for aa in seq:
    print(aa.getMonoWeight())


# In[8]:


sum=0
for aa in seq:
    sum +=aa.getMonoWeight()
print(sum)


# In[ ]:




