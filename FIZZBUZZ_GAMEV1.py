# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:52:09 2023

@author: vidha
"""

n=input("Provide value upto which you want to play game Lets play this game!! ")
n=int(n)
for i in range(n):
 if(i%15==0):
    print("FizzBuzz",i)
 else: 
    if(i%15!=0):
        if(i%3==0):
             print('Fizz',i)
        else:     
          if(i%5==0):
             print("Buzz",i)
          else:
             print(i,"useless")