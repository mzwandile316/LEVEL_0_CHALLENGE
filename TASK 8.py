#!/usr/bin/env python
# coding: utf-8

# # Task 8

# In[7]:


def convert_number(minutes):
    minutes = minutes % (24 * 60)
    hour = minutes // 60
    minutes %= 60
    return "%d Hour:%02d minutes" % (hour, minutes)

number = int(input("Enter number "))
convert_number(number)


# In[ ]:




