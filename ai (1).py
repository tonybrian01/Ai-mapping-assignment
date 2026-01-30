#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import random


# In[9]:


dataset=pd.read_csv('survey.csv',sep=';')
print(dataset.head())


# In[10]:


cost=[]
for i in range(len(dataset)):
    cost.append(random.randint(1,26))
print(cost)


# In[11]:


search_graph={

}
for i in range(len(dataset)):
    search_graph[i]=[cost[i],[dataset.iloc[i,1]],dataset.iloc[i,2],dataset.iloc[i,0]]
for i in range(len(dataset)):
    print(search_graph[i])


# In[12]:


get_ipython().system('pip install haversine')


# In[13]:


import haversine
from haversine import haversine
i=0
distance=[]
while i<len(dataset):
    j=1
    while j<len(dataset):
        column1=(dataset.iloc[i,0],dataset.iloc[i,1])
        column2=(dataset.iloc[j,0],dataset.iloc[j,1])
        distance.append(haversine(column1,column2))
        j+=1
    i+=1
print(distance)




# In[16]:


search_graph={

}
i=0
while i <len(dataset):
    search_graph[i]=[distance[i],dataset.iloc[i,0],dataset.iloc[i,2],dataset.iloc[i,0]]
    i+=1
i=0
while i <len(dataset):
    print(search_graph[i])
    i+=1


# In[20]:


import folium
m = folium.Map(location=[dataset.iloc[0,0],dataset.iloc[0,1]],zoom_start=15)
for i, row in dataset.iterrows():
    folium.Marker(
        location=[row['latitude'],
row['longitude']],
        popup=row['location'],
        tooltip=row['location']
    ).add_to(m)
m


# In[21]:


final_graph={}
metters_to_km = 1000
for i in range(len(dataset)):
    lat = dataset.iloc[i,0]
    long = dataset.iloc[i,1]
    loc = dataset.iloc[i,2]
    dist_km = distance[i] / metters_to_km
    final_graph[loc] = ([long,lat,loc,dist_km],)

import pprint
pprint.pprint(final_graph)


# In[23]:


final_graph = {}

for i in range(len(dataset) - 1):
    curr_name = dataset.iloc[i, 2]
    curr_long = dataset.iloc[i, 1]
    curr_lat = dataset.iloc[i, 0]


    next_idx = i + 1
    next_long = dataset.iloc[next_idx, 1]
    next_lat = dataset.iloc[next_idx, 0]


    d_val = distance[i] 
    c_val = cost[i]     


    final_graph[curr_name] = (
        [curr_long, curr_lat, d_val, c_val],
        [next_long, next_lat, d_val, c_val]
    )

import pprint
pprint.pprint(final_graph)


# In[ ]:




