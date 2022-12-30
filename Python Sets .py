#!/usr/bin/env python
# coding: utf-8

# In[1]:


thisset = {"apple", "banana", "cherry"}
print(thisset)


# In[2]:


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# In[3]:


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# In[4]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[5]:


thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)


# In[6]:


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# In[ ]:




