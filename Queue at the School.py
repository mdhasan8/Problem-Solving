# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:24:20 2021

@author: Easin
"""

n,t = input().split()
n = int(n)
t = int(t)
in1 = input()
in1 = list(in1)

for val in range(t):
    flag = True
    for elem in range(len(in1)-1):
        #print(in1)
    
        if in1[elem] == 'B' and in1[elem+1] == 'G' and flag == True:
            in1[elem] = 'G'
            in1[elem+1] = 'B'
            flag = False
            
        else:
            flag = True
        
in2 = ''.join(in1)    
print(str(in2))
