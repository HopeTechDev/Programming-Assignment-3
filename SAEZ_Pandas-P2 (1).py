#!/usr/bin/env python
# coding: utf-8

# ### Experiment 3 - Problem 2

# In[13]:


import pandas as pd #import pandas library

cars = pd.read_csv("cars.csv") #load the .csv file into a data frame named cars using pandas

# For Letter A
cars.iloc[:,::2].head() # Use iloc to get your desired columns to display, specifically the columns that are odd-numbered.
# : to display all rows
# ::2 to start at the beginning and step by 2.


# In[15]:


# For letter B.
cars.loc[cars['Model']=='Mazda RX4']


# In[21]:


# For letter C.
cars.loc[cars['Model']=='Camaro Z28', ['Model','cyl']]


# In[19]:


# For letter D.
models = ('Mazda RX4 Wag','Ford Pantera L','Honda Civic') # Set up a tuple for the models of the cars
cars.loc[cars['Model'].isin(models),['Model','cyl','gear']] # Use the .isin() function so that it can identify the elements of the variable in the dataframe.

