#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_side = float(input("Ënter the number of first side "))
second_side = float(input("Enter the number of second side "))
third_side = float(input("Enter the number of third side "))

def area(first_side,second_side,third_side):
    if (first_side < 0 or second_side < 0 or third_side < 0 or (first_side + second_side <= third_side) or (third_side + first_side <= second_side) or (second_side + third_side <= first_side)):
        print("no area")
        return

# The semi-perimeter calculation
    semi_perimeter = (first_side + second_side + third_side) / 2

#The calculation of area
    area = (semi_perimeter*(semi_perimeter-first_side)*(semi_perimeter-second_side)*(semi_perimeter-third_side))**0.5
    print('The area of the triangle is %f' %area)

area(first_side, second_side, third_side)


# In[ ]:




