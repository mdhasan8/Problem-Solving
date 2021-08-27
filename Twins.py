# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:34:46 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
in2 = input().split()
list1 = []
for val in range(in1):
    in3 = int(in2[val])
    list1.append(in3)

#print(list1)
sum1 = 0
for elem in range(len(list1)):
    sum1 += list1[elem]
#print(sum1)
avrg = sum1/2

list1.sort()
sum2 = 0
for elements in range(len(list1)):
    sum2 += list1[-elements-1]
    if sum2 > avrg:
        print(elements+1)
        break
    
    
        
        
    