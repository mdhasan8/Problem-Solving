# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:20:40 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
list1 = []
for elem in range(len(in2)):
    list1.append(int(in2[elem]))
    
#print(list1)

amazing = 0
min1 = list1[0]
max1 = list1[0]

for val in range(len(list1)-1):
    if list1[val +1] > min1:
        
        amazing +=1
        min1 = list1[val+1]
    elif list1[val +1] < max1:
        amazing += 1
        max1 = list1[val+1]
print(amazing)
    
        
        