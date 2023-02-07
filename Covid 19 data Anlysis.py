#!/usr/bin/env python
# coding: utf-8

# # Covid-19  Confirmed Death Recovered and Active cases analysis

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


df=pd.read_csv(r'C:\Users\Anusha\Desktop\country_wise_latest.csv')
df.head(5)


# In[14]:


df.columns


# In[15]:


df.shape


# In[16]:


df.index


# In[17]:


df.rename(columns={'Country/Region':'country'},inplace=True)


# In[18]:


df.head()


# In[19]:


df.info()


# In[20]:


df1=df[df['Confirmed']>100]
df1


# In[21]:


countries=df['country'].unique()
len(countries)


# In[23]:


for idx in range(0,len(countries)):
    C=df[df['country']==countries[idx]].reset_index()
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='red',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='green',label='Deaths')
    plt.scatter(np.arange(0,len(C)),C['Active'],color='green',label='Active')
    plt.title(countries[idx])
    plt.xlabel("days suspect")
    plt.ylabel("number of cases")
    plt.legend()
    plt.show()


# In[ ]:




