# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:56:57 2023

@author: vidha
"""
def stone_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    print(p1)
    print(p2)
    if(player_one[p1]==player_two[p2]):
        print("This match is draw")
    elif(player_one[p1]=='Rock' and player_two[p2]=='Scissor'):
        print("Player 1 won!!!")
    elif(player_one[p1]=='Rock' and player_two[p2]=='Paper'):
        print("player 2 won!!")
    elif(player_one[p1]=='Paper' and player_two[p2]=='Scissor'):
        print("player 2 won!!")
    elif(player_one[p1]=='Paper' and player_two[p2]=='Rock'):
        print("Player 1 won!!!")
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Rock'):
        print("player 2 won!!")
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Paper'):
         print("Player 1 won!!!")




player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Rock',1:'Paper',2:'Scissor'}

while(1):
    num1=input("player one please enter choice")
    num2=input("player  two please enter choice")
    bit1=int(input('P1 enter your secret position bit'))
    bit2=int(input('p2 enter your secret position bit '))
    stone_paper_scissor(num1,num2,bit1,bit2)
    ch=input('Do you want to continue the game (y/n)')
    if(ch=='n'):
        break