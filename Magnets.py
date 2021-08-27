# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:18:57 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
list1 = []
count = 1
for val in range(in1):
    list1.append(input())
for elem in range(len(list1)-1):
    for elem1 in range(elem+1,elem+2):
        #print('1st loop',list1[elem])
        #print('2nd loop',list1[elem1])
        if list1[elem] != list1[elem1]:
            
            count += 1
    
print(count)    