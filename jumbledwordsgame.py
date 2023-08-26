# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:20:02 2023

@author: vidha
"""
import random
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick
def play():
    p1name=input('Player 1,Please enter your name')
    p2name=input('player2,Please enter your name')
    Pp1=0
    Pp2=0
    turn=0
    c=1
    while(c==1):
        #computer task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        if(turn%2==0):
            print(p1name,'Your turn')
            ans1=input('Please input your ans')
            if(ans1==picked_word):
                Pp1=Pp1+1
                print(Pp1,'Hurray! you guess it right')
            else:
                print('opps you are wrong')
        else:
            print(p2name,'Your turn')
            ans2=input('Please input your ans')
            if(ans2==picked_word):
                Pp2=Pp2+1
                print(Pp2,'Hurray! you guess it right')
            else:
                print('opps you are wrong correct answer is',picked_word)
        turn=turn+1
        p1o=int(input('Do you want to continue p1'))
        if(p1o==0):
            c=0
            print('Thankyou for playing')
        p2o=int(input('Do you want to continue p2'))        
        if(p2o==0):
            c=0
            print('Thankyou for playing')
    print(p1name,'=',Pp1,p2name,'=',Pp2)
play()     
            