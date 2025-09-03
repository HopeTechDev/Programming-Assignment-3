#!/usr/bin/env python
# coding: utf-8

# #### SAEZ, Eljenzal Hoper U. 

# ## *Pandas - Part 1*

# ###### a. Load the corresponding .csv file into a data frame named cars using pandas (http://bit.ly/Cars_file)
# ###### b. Display the first five and last five rows of the resulting cars.
# ###### c. Save your file as Surname_Pandas-P1.py

# In[5]:


import pandas as pd #import pandas library

cars = pd.read_csv("cars.csv") #load the .csv file into a data frame named cars using pandas
p1 = pd.concat([cars.head(), cars.tail()]) #display the first 5 rows and last 5 rows of cars.csv
p1

