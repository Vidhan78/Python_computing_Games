# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:27:07 2023

@author: vidha
"""
i=1
while(i==1):
 import random
 movies=['anand','drishyam','nayakan','anbe sivam','gol maal','vikram vedha','black friday','dangal','manichithrathazu','taare zameen par']
 move=list(random.choice(movies))
 num=len(move)
 test=''.join(move)

 
 
 point=10
 print('you have given with',point,'points once you loose it you have try with other word or exit game')
 print
 ans=[0]*num
 print(ans)

 print('the length of the  movie name is',num)

 while(point>=0):
 
  inp=input(' letter you think might be in movie name')
 

  for i in range(num):
    if(inp==move[i]):
        ans.insert(i,inp)
        ans.pop(i+1)
  print(ans)
  right=input('ARE YOU ABLE TO GUESS MOVIE PLEASE ENTER YOUR GUESS')
  if(right==test):
     print('you have cracked it win!!!')
     point=-1
  else:
     point=point-1
     print('you were wrong try be discovering other letters but your points are now',point)
 
 i=int(input('Do you want to try again with some other word? yes-1,No-0'))
 
    