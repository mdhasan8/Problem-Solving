# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:53:55 2021

@author: Easin
"""

n,m = input().split()
n = int(n)
m = int(m)


for elem in range(n):
    str1 = ''
    if elem % 2 == 0:
        for val in range(m):
            str1 += "#"
    elif elem%4 == 1:
        
        for val1 in range(m-1):
            str1 += "."
        str1 += "#"
    elif elem%4 == 3:
        str1 += "#"
        
        for val1 in range(m-1):
            str1 += "."
        
    
    
    print(str1)
    

    