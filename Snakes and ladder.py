# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:21:48 2023

@author: vidha
"""

from PIL import Image
end=100
import random
def show_board():
    img=Image.open("D:\slb.jpg")
    img.show()

def play():
    #input player 1 name
    p1_name= input("Player 1 ,please enter your name:")
    #input player 2 name
    p2_name= input("Player 2 ,please enter your name:")
    #intial points for player1
    pp1=0
    #intial points for player1
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            #player 1 turn
            print(p1_name,'your turn')
            #ask player  choice to continue 
            c=input('press 1 to continue ,0 to quit:')
            if c==0:
             print(p1_name,'scored',pp1)
             print(p2_name,'scored',pp2)
             print('Quitting the game ,Thanks for playing')
             break
            #generate  a random  number from 1,2,3,4,5,6
            dice=random.randint(1,6)
            print('Dice showed:',dice)
            #add points 
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            print(p1_name,'your score:',pp1)
            #check if player goes beyond the board 
            if dice==6:
                continue
            if pp1>end:
             pp1=end
             print(p1_name,'your score:',pp1,'congratulations')
             break
            turn=turn+1 
            print()
            print()
        else:
            
                #player 2 turn
                print(p2_name,'your turn')
                #ask player  choice to continue 
                c=input('press 1 to continue ,0 to quit:')
                if c==0:
                 print(p1_name,'scored',pp1)
                 print(p2_name,'scored',pp2)
                 print('Quitting the game ,Thanks for playing')
                 break
                #generate  a random  number from 1,2,3,4,5,6
                dice=random.randint(1,6)
                print('Dice showed:',dice)
                #add points 
                pp2=pp2+dice
                pp2=check_ladder(pp2)
                pp2=check_snake(pp2)
                print(p2_name,'your score:',pp2)
                if dice==6:
                    continue
                #check if player goes beyond the board 
                if pp2>=end:
                 pp2=end
                 print(p2_name,'your score:',pp2,'congratulations')
                 break
                turn=turn+1
                print()
                print()
def check_ladder(points):
    if points==8:
        print('Ladder')
        return 26
    elif points==21:
        print('Ladder')
        return 82
    elif points==43:
        print('Ladder')
        return 77
    elif points==50:
        print('Ladder')
        return 91
    elif points==54:
        print('Ladder')
        return 93
    elif points==62:
        print('Ladder')
        return 96
    elif points==66:
        print('Ladder')
        return 87
    elif points==80:
        print('Ladder')
        return 100
    else:
        #Not a ladder 
        return points
def check_snake(points):
    if points==44:
        print('snake')
        return 22
    elif points==46:
        print('snake')
        return 5
    elif points==48:
        print('snake')
        return 9
    elif points==52:
        print('snake')
        return 11
    elif points==55:
        print('snake')
        return 7
    elif points==59:
        print('snake')
        return 17
    elif points==64:
        print('snake')
        return 36
    elif points==69:
        print('snake')
        return 33
    elif points==73:
        print('snake')
        return 1
    elif points==83:
        print('snake')
        return 19
    elif points==92:
        print('snake')
        return 51
    elif points==95:
        print('snake')
        return 24
    elif points==98:
        print('snake')
        return 28
    else:
        #not a snake
        return points
    
show_board()
play()
    
        
        