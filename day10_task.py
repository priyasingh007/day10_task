#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("D:\Downloads\heart.csv")
df


# In[3]:


type(df)


# In[4]:


df.shape


# In[5]:


df.describe()


# In[7]:


df["age"]


# In[8]:


df.iloc[2]


# In[9]:


df.loc[2]


# In[10]:


df.iloc[[3,2,1]]


# In[11]:


df[:3]


# In[12]:


df[['chol','fbs','thall']][:3]


# In[14]:


df.chol.iloc[[2]]


# In[16]:


df[df.age > 67].head()


# In[20]:


#data cleaning
#removing duplicates rows
series = df.duplicated()
series


# In[21]:


df.drop_duplicates(inplace = True)
df.head(4)


# In[ ]:


#data aggregation


# In[22]:


df.agg(['min','max'])


# In[23]:


df['age'].max()


# In[24]:


df['age'].min()


# In[25]:


df['age'].median()


# In[26]:


df['age'].sum()


# In[27]:


df['age'].std()


# 
