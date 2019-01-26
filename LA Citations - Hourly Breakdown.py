#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

import gmaps
import gmaps.datasets
from datetime import date
from datetime import time
import seaborn as sns
from matplotlib.pyplot import figure

sns.set(color_codes=True)


# In[108]:


df1 = pd.read_csv("Desktop/LA Citations 2018/LA-Crime-Project-2018/out2.csv")


# In[109]:


df1.head(10)


# In[110]:


#remove rows with Nan values

df1.replace(["NaN", 'NaT'], np.nan, inplace = True)
df1 = df1.dropna()

#check Nan values were dropped from Issue Time column

df1[df1["Issue time"].isnull()]


# In[111]:


#remove last four characters - leave hour digits
#add leading zeroes to equalize lenght

df1['Issue time'] = df1['Issue time'].apply(lambda x: str(int(x)).zfill(4))
df1['Issue time'] = df1['Issue time'].map(lambda x: str(x)[:-2])


# In[112]:


#verify Issue time is in correct format

df1["Issue time"].sample(10)


# In[100]:


# group = df1.groupby(['Issue time','Violation code']).agg({"Violation Description":"first","Ticket number":"count"})
# #.sort_values(by='Ticket number',ascending=False)
# group1 = group[group['Ticket number'] > 10000]
# group1


# In[101]:


# df1.groupby(df1["Issued Date"].dt.month).count().plot(kind="bar", legend=False, color="b")
# plt.show()


# In[113]:


#group by to get citation count per hour

newdf = df1.groupby("Issue time").count()
newdf.sort_values('Issue time', ascending=True)
newdf


# In[114]:


#new df for graph data

final_chart1 = newdf[["Ticket number"]]
final_chart1= final_chart1.rename(index={"00":"12am","01":"1am","02":"2am","03":"3am","04":"4am","05":"5am","06":"6am","07":"7am","08":"8am","09":"9am","10":"10am","11":"11am","12":"12pm","13":"1pm","14":"2pm","15":"3pm","16":"4pm","17":"5pm","18":"6pm","19":"7pm","20":"8pm","21":"9pm","22":"10pm","23":"11pm"})
final_chart1


# In[125]:


#build chart

final_chart1.plot(kind='bar',legend=False,color="purple",width=.7, alpha=0.7, figsize=(15,10), fontsize=14)
plt.xlabel("Time",fontsize=14)
plt.ylabel("Number of Citations",fontsize=17)
plt.title("Total Citations per Hour",fontsize=20)

plt.savefig("hourly_citations.png")

plt.show()


# ## Analysis
# The graph shows a drastic jump in issued tickets starting at 8am and lasting throughout noon, wherafter the number of citations start to decrease. Most of the citations were issued at 8am, 10am, and noon.

# In[ ]:




