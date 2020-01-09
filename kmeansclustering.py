#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns


# In[2]:


import matplotlib.pyplot as plt 

from sklearn.datasets import make_blobs


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data=make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8,
               random_state=101)


# In[5]:


data


# In[6]:



plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')


# In[7]:


data[1]


# In[8]:


from sklearn.cluster import KMeans


# In[9]:


kmeans= KMeans(n_clusters=4)


# 

# In[10]:


kmeans.fit(data[0])


# In[11]:


kmeans.cluster_centers_


# In[30]:


kmeans.labels_


# In[29]:


fig, (ax1,ax2)=plt.subplots(1,2, sharey=True,figsize=(10,6))


# In[31]:


ax1.set_title("predicted data")


# In[ ]:





# In[33]:


ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')


# In[38]:


ax2.set_title("orginal data")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')

