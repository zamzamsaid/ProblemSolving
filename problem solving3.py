#!/usr/bin/env python
# coding: utf-8

# In[1]:


height = int(input("Enter the height of the triangle: "))

for row in range(height):
    print(" " * (height - row - 1) * 2, end="")
    for i in range(row + 1):  
        print(2 ** i, end=" ")
        
    for i in range(row - 1, -1, -1): 
        print(2 ** i, end=" ")
    
    print()


# In[ ]:




