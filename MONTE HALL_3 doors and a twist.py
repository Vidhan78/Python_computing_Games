# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:27:07 2023

@author: vidha
"""

import random
doors=[0]*3
goatdoor=[0]*2
swap=0#No of swap wins
dont_swap=0#no of dont swap wins
j=0
for j in range(10):
 x=random.randint(0,2)#xth door will comprise of BMW
 doors[x]='BMW'
 for i in range (0,3):
    if(i==x):
        continue
    else:
        doors[i]='goat'
        goatdoor.append(i)
 choice=int(input('Enter your choice'))
 door_open=random.choice(goatdoor)#open a door only comprise of goat
 while(door_open==choice):#door open should not equal to choice made by participants
    door_open=random.choice(goatdoor)
 print(door_open,'this is a door which has goat ')
 ch=input("DO YOU WANT TO SWAP?y/n")
 if(ch=='y'):
    if(doors[choice]=='goat'):
     print('player wins')
     swap=swap+1
    else:
     print('player lost')
 else:
    if(doors[choice]=='goat'):
        print('player lost')
    else:
        print('player wins')
        dont_swap=dont_swap+1
 print(swap)
 print(dont_swap)
 