#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = int(input("Enter your number= "))
resultodd = 0
resulteven = 0
for i in range(1,number+1):
    if i % 2 == 0:
        resulteven += i 
    else:
        resultodd += i 
print("summary of odd numbers: ",resultodd )
print("avarege of even numbers : ", resulteven/2 )


# In[ ]:




