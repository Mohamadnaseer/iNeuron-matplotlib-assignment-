#!/usr/bin/env python
# coding: utf-8

# #   Matplotlib
# 
# 

# # Scipy:

# We have the min and max temperatures in a city In India for each months of the year.
# We would like to find a function to describe this and show it graphically, the dataset
# given below.
# Task:
# 1. fitting it to the periodic function
# 2. plot the fit
# Data
# Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
# Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18
# 

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


import numpy as np
temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

import matplotlib.pyplot as plt
months = np.arange(12)
plt.plot(months, temp_max, 'go')
plt.plot(months, temp_min, 'co')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')


# # 1. fitting it to the periodic function

# In[7]:


from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 1.8 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      temp_max, [40, 20, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      temp_min, [-40, 20, 0])


# # 2. plot the fit

# In[10]:


days = np.linspace(0, 12, num=365)
plt.figure()
plt.plot(months, temp_max, 'go')
plt.plot(days, yearly_temps(days, *res_max), 'm-')
plt.plot(months, temp_min, 'co')
plt.plot(days, yearly_temps(days, *res_min), 'y-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()


# # Matplotlib:
This assignment is for visualization using matplotlib:
data to use:
url=https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv
titanic = pd.read_csv(url)
# # 1. Create a pie chart presenting the male/female proportion

# In[22]:


url = "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic = pd.read_csv(url)


# In[23]:


titanic.head()
x = titanic["sex"]
Dummy = pd.get_dummies(x)
T = pd.concat((titanic , Dummy),axis = 1)
T1 = T.drop(["sex","male" ],axis = 1)
T1.head()


# In[25]:


x = T1["female"]
Col = pd.Series(x, dtype=int)


# In[27]:


Total_female = sum(Col)
for i in Col.shape:
    row = i
    break
Total_male = abs(row - Total_female)
L = [Total_male , Total_female]
plt.title('Male/Female Proportion')
plt.pie(L,labels = [ "male ", "female "],autopct="%0.2f%%")
plt.show()


# # 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# In[28]:


plt.title('scatterplot with the Fare paid and the Age',fontsize=25)
plt.xlabel('Fare',fontsize=20)
plt.ylabel('Age',fontsize=20)
sns.scatterplot(y=titanic["fare"], x=titanic["age"], hue=titanic["sex"])
plt.figure(figsize=(8,6))

