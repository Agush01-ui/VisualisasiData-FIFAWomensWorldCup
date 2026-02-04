#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file_path = r"C:\Users\LENOVO\Downloads\womens-world-cup.csv"
df = pd.read_csv(file_path)

df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isna().sum()


# In[6]:


df = df.rename(columns={
    "possesion": "possession"
})


# In[7]:


df.columns = df.columns.str.lower().str.strip()


# In[8]:


df["possession"] = df.groupby("year")["possession"].transform(
    lambda x: x.fillna(x.mean())
)


# In[9]:


df["yellow_cards"] = df["yellow_cards"].fillna(0)
df["red_cards"] = df["red_cards"].fillna(0)


# In[10]:


df["yellow_cards"] = df["yellow_cards"].astype(int)
df["red_cards"] = df["red_cards"].astype(int)


# In[11]:


df.isna().sum()


# In[12]:


df["possession"] = df["possession"].fillna(df["possession"].mean())


# In[13]:


df.isna().sum()


# In[14]:


df.info()


# In[15]:


df.duplicated().sum()


# In[16]:


df[(df["age"] < 15) | (df["age"] > 45)]


# In[17]:


df[(df["possession"] < 20) | (df["possession"] > 80)]


# In[18]:


df["squad"].value_counts()


# In[19]:


sorted(df["year"].unique())


# In[20]:


df["yellow_cards"].unique()
df["red_cards"].unique()


# In[21]:


df.describe()


# In[22]:


df


# In[23]:


import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# In[24]:


df


# In[25]:


clean_path = r"C:\Users\LENOVO\Downloads\womens-world-cup-clean.csv"
df.to_csv(clean_path, index=False)


# In[26]:


import os
os.path.exists(clean_path)


# In[ ]:




