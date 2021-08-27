# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:21:29 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
list1 = []
for elem in range(in1):
    input2 = int(in2[elem])
    list1.append(input2)
list2 = []
for val in range(len(list1)):
    #print(val)
    for val2 in range(len(list1)):
        #print(val2)
        if list1[val2] == val+1:
            list2.append(val2+1)
    
    
print(*list2)