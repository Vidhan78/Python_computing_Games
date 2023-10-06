# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:33:50 2023

@author: vidha
"""

import numpy 
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
#(-)hyphen denotes empty in numpy
p1s='X'
p2s='0'
def check_rows(symbol):
  for r in range(3):
      count=0
      for c in range(3):
          if board[r][c]==symbol:
              count=count+1
      if count==3:
          print(symbol,'won')
          return True
  return False
def check_cols(symbol):
  for c in range(3):
      count=0
      for r in range(3):
          if board[r][c]==symbol:
              count=count+1
      if count==3:
          print(symbol,'won')
          return True
          #when you return something the functionality comes to an end doest not compile further      
  return False
def check_digaonals(symbol):
    count=0
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==symbol:
        print(symbol,'won')
        return True
    for i in range(3):
     if(board[i][i]==symbol):
            count+=1
    if count==3:
        print(symbol,'won')
        return True
    return False            

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_digaonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input('Enter row-1 or 2 or 3:'))
        col=int(input('Enter col-1 or 2 or 3:'))
        if row>0 and row<4 and col>0 and col<4 and board[row-1] [col-1]=='-':
            break
        else:
            print('Invalid input, Please enter again')
    board[row-1][col-1]=symbol
def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
                print('0 turn')
                place(p2s)
                if won(p2s):
                    break
    if not(won(p1s)) and not(won(p2s)):
         print('draw')
play()