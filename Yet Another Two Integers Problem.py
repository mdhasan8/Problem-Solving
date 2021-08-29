# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:54:04 2021

@author: Easin
"""

t = input()
t = int(t)

for elem in range(t):
    a,b = input().split()

    a = int(a)
    b = int(b)
    if a != b and ((a-b)%10 ==0 or (b-a)%10==0):
        print((abs(a-b)//10))
    elif a != b:
        print((abs(a-b)//10) + 1)
    
    elif a==b:
        print(0)
        
    
'''
    if a > b:
        count = 0
        while a > b:
            #count = 0
            a = a - 10
            count += 1
        print(count)
    
    elif a < b:
        #print(a)
        count = 0
        while a < b:
            #count = 0
            a = a + 10
            count += 1
        print(count)
        
    elif a == b:
        print(0)
'''
          