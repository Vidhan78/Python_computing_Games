# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:46:14 2023

@author: vidha
"""

import string
import random
symbols=list(string.ascii_letters)# we are asigning string data type to symbol hence it will not act as list need to convert in list
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
#pos1 and pos2 are samesymbol  positions for card1 and card2
if(pos1==pos2):
    card1[pos1]=samesymbol
    card2[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    alphabet1=random.choice(symbols)
    symbols.remove(alphabet1)
    alphabet2=random.choice(symbols)
    symbols.remove(alphabet2)
    card1[pos2]=alphabet1
    card2[pos1]=alphabet2
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)
ch=input('the same symbol you think')
if(ch==samesymbol):
    print('hurray! you are right')
else:
    print('you are wrong')
        
    