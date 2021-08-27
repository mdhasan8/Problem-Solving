# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:37:53 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

flag = False
while (flag == False):
    list1 = []
    x = in1+1
    in1 = in1 + 1
    for elem in range(4):
        list1.append(x%10)
        x = x//10
    #print(list1)
    flag = True
    for val in range(len(list1)):
        for val1 in range(val+1,len(list1)):
            
            if list1[val] == list1[val1]:
                flag = False
                break
print(in1)
    
        
            
       

 