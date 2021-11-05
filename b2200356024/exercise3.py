#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# guess the number
import random

# print(""" *****************
# guess the number between 1- 40
# *****************
#
# """)
randomnumber = random.randint(1,40)
guessright= 7
while True:
    guess = int(input("enter your guess: "))

    if guess < randomnumber:
        print("loading...")
        
        print("guess a bigger number!")
        guessright -= 1
    elif guess > randomnumber:
        print("loading...")
        
        print("guess a smaller number!")
        guessright -=1
    else:
        print("loading...")
       
        print("congrats !!! you nailed it ")
        break
    if guessright == 0:
        print("your rigt is over ")
        break


# In[ ]:




