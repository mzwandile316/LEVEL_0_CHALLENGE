#!/usr/bin/env python
# coding: utf-8

# # Task 10

# In[9]:


from collections import Counter

def common_letter(word_1,word_2):
    dictionary_1 = Counter(word_1)
    dictionary_2 = Counter(word_2)
    
    common_distionary = dictionary_1 & dictionary_2
    
    if len(common_distionary) == 0:
        print(-1)
        return
    
    common_elements = list (common_distionary.elements())
    print ("".join(common_elements))

word_1 = input("Enter first word ")
word_2 = input("Enter second word ")
common_letter(word_1,word_2)


# In[ ]:




