# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:20:49 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()


list1 = []

for element in range(in1):
    in2[element] = int(in2[element])
var = sorted(in2)
for vals in range(len(var)):
    print(var[vals],end=' ')




'''
for elem in range(in1):
    for val in range(elem+1,len(in2)):
        if in2[elem] >= in2[val]:
            flag = True
            
    if flag == True:
            
        list1.append(in2[elem])
        flag = False
        print(list1)
            
'''        
    

