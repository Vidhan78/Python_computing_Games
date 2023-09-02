# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:49:03 2023

@author: vidha
"""
n=input('please insert odd n for which you want nxn magic square matrix')
n=int(n)

def squarematrix(n):
    matrix=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        matrix.append(l)
    print(matrix)
    num=n*n
    count=1
    i=n//2
    j=n-1
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i==-1):
                i=n-1
            if(j==n):
                j=0
        if(matrix[i][j] !=0):
            i=i+1
            j=j-2
            continue #it will skip executing whatever is written after this line
        else:
            matrix[i][j]=count
            count=count+1
            i=i-1
            j=j+1
    for i in range(n):
        for j in range(n):
           print(matrix[i][j],end=' ')
        print()
squarematrix(n)
print('the sum of each row/column/diagonal is:',(n*(n**2+1))//2)        
     
            