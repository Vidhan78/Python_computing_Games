# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:52:10 2023

@author: vidha
"""

c=1
while(c==1):
 n=input("Provide NUmber Lets play this game!! ")
 n=int(n)
 
 if(n%15==0):
    print("FizzBuzz")
 if(n%15!=0):
        if(n%3==0):
             print('Fizz')
        else:    
         if(n%5==0):
             print("Buzz")
         else:
             print(n,"is useless")
 c=input("Do you want to continue the game yes-1,no-0 (0/1)")
 c=int(c)