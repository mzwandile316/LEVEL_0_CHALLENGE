#!/usr/bin/env python
# coding: utf-8

# # Task 6

# In[2]:


first_num = int(input("Enter number "))
second_num = int(input("Enter number "))
third_num = int(input("Enter number "))

def maximum_number(first_num,second_num,third_num):
    if (first_num >= third_num) and (first_num >= second_num):
        print(first_num, "is the maximum number")
    elif (second_num >= first_num) and (second_num >= third_num):
        print(second_num, "is the maximum number")
    elif (third_num >= second_num) and (third_num >= first_num):
        print(third_num, "is the maximum number")
        
        
maximum_number(first_num,second_num,third_num)


# In[3]:


first_num = int(input("Enter number "))
second_num = int(input("Enter number "))
third_num = int(input("Enter number "))
fourth_num = int(input("Enter number "))

def maximum_number(first_num,second_num,third_num):
    if (first_num >= third_num) and (first_num >= second_num) and (first_num >= fourth_num):
        print(first_num, "is the maximum number")
    elif (second_num >= first_num) and (second_num >= third_num) and (second_num >= fourth_num):
        print(second_num, "is the maximum number")
    elif (third_num >= second_num) and (third_num >= first_num) and (third_num >= fourth_num):
        print(third_num, "is the maximum number")
    elif (fourth_num >= first_num) and (fourth_num >= second_num) and (fourth_num >= third_num):
        print(fourth_num, "is the maximum number")
        
        
maximum_number(first_num,second_num,third_num)


# In[ ]:




