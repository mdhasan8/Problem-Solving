# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:37:17 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)
for elements in range(in1):
    in2 = input()
    in2 = int(in2)
    a = input().split()
    
    list1 = []
    for elem in range(len(a)):
        list1.append(int(a[elem]))
    list1.sort()
    
    flag = True
    for val in range(len(list1)-1):
        flag = False
        #print(val)
        for val2 in range(val+1,len(list1)):
            #print(abs(list1[val] - list1[val2]))
            if abs(list1[val] - list1[val2]) <= 1:
                flag = True
                break
        
        if flag == False:
            #print(val)
            break
    if flag == True:
        print("YES")
    elif flag == False:
        print("NO")
        
                    
        