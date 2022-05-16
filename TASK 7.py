#!/usr/bin/env python
# coding: utf-8

# # Task 7

# In[4]:


#Celsius to Fahrenheit

celsius = float(input("Enter the temperature in celsius "))
fahrenheit = (celsius * 9/5) + 32

print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))


# In[5]:


#Fahrenheit to celsius

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))


# In[ ]:




