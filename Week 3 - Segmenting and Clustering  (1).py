
# coding: utf-8

# In[1]:



import numpy as np 
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


wiki_url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

raw_wiki= requests.get(wiki_url).text
soup = BeautifulSoup(raw_wiki,'html5lib')


# In[3]:


table=soup.find('table')


# In[4]:


Postcode= []
Borough= []
Neighbourhood = []


# In[5]:


x=0 #counter
for table_cell in table.find_all('td'):
    
    x = x+1
    if (x==1):
        postal_code = table_cell.text
    elif (x==2):
        borough = table_cell.text
    elif (x==3):
        neighborhoods_data = table_cell.text
        neighborhoods = neighborhoods_data.strip('\n')
        x=0 #reset counter
                             
        if borough == 'Not assigned':            
            borough = []
            neighborhoods_data=[]
        else:
            if neighborhoods == 'Not assigned':
                neighborhoods = borough
             
            Postcode.append(postal_code)
            Borough.append(borough)
            Neighbourhood.append(neighborhoods)


# In[6]:


data=[]

for postcode_unique_element in set(Postcode):
    post_value = ''
    borough_value_var = ''
    neighbourhood_value = ''
    
    for postcode_idx, postcode_element in enumerate(Postcode):
        if postcode_unique_element == postcode_element:
            post_value = postcode_element;
            borough_value_var = Borough[postcode_idx]
            
            if neighbourhood_value == '': 
                neighbourhood_value = Neighbourhood[postcode_idx]
            else:
                neighbourhood_value = neighbourhood_value + ', ' + Neighbourhood[postcode_idx]
    
    data.append([post_value,borough_value_var,neighbourhood_value])

df = pd.DataFrame(np.array(data),columns=['PostalCode', 'Borough', 'Neighborhood'])
df.head(14)


# In[7]:


df.describe()

