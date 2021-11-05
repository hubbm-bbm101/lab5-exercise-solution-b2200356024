#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mail = input("Enter your mail: ")
listn = list(mail)
print(listn)
if listn.count("@") ==1 and listn.count(".") > 0 :
    print(f" the mail ({mail}) is verified.")
else:
    print(f"the mail ({mail}) is not verified.")


# In[ ]:




