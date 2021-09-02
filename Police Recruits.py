# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:58:50 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input().split()
list1 = []
for val in range(len(in2)):
    
    in3 = int(in2[val])
    list1.append(in3)
#print(list1)

police = 0
untreat = 0

for elem in range(len(list1)):
    if list1[elem] == -1 and police ==0:
        untreat +=1
    elif list1[elem] == -1 and police !=0:
        police = police - 1
    elif list1[elem] != -1:
        police = police + list1[elem]
print(untreat)
        