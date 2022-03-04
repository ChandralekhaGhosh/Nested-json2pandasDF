#!/usr/bin/env python
# coding: utf-8

# In[42]:


#### Converting a nested json to pandas dataframe


# In[1]:


import pandas as pd


# In[3]:


#The URL
url="https://api.github.com/repos/pandas-dev/pandas/issues"


# In[7]:


#To get the priginal json file

import requests
data=requests.get(url)


# In[8]:


data


# In[9]:


#To read the file
data1=data.json()


# In[19]:


data1


# In[30]:


df1 = pd.DataFrame(data1 , columns=['id','url' , 'repository_url' , 'labels_url','user'])
df1


# In[31]:


#Unwrapping the nested list 'user' and converting its keys into a list of dict
df2=[]
for i in df1['user']:
    df2.append(i)
df2            
    


# In[32]:


#Convering the list into a pandas dataframe,df2
df2=pd.DataFrame(df2)
df2  
#It has unwrapped the user dictionary and converted the keys as column names and values as rows


# In[40]:


#Now appending with the earlier dataset df1 and creating a new dataset, df
df=pd.concat([df1,df2],axis=1)
pd.DataFrame(df)


# In[41]:


#saving the dataframe into a csv file
df.to_csv('unwrapped.csv')


# In[ ]:




