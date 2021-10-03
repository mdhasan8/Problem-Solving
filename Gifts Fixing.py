# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:52:01 2021

@author: Easin
"""
t = input()
t = int(t)
for elements in range(t):
    
    in1 = input()
    in1 = int(in1)
    
    in2 = input().split()
    list1 = []
    
    for elem in range(len(in2)):
        x = in2[elem]
        list1.append(int(x))
        
    in3 = input().split()
    list2 = []
    
    for elem in range(len(in3)):
        y = in3[elem]
        list2.append(int(y))
        
    #print(list1)
    #print(list2)
    m = min(list1)
    n = min(list2)
    count = 0
    count2 = 0
    list3 = []
    list4 = []
    for val1 in range(len(list1)):
        count = count + (list1[val1] - m)
        p = (list1[val1] - m)
        list3.append(p)
        
    
    for val2 in range(len(list2)):
        count = count + (list2[val2] - n)
        q = (list2[val2] - n)
        list4.append(q)
    
    for vals in range(len(list3)):
        
        if list3[vals] != 0 and list4[vals] !=0:
            count2 += min(list3[vals], list4[vals])
    print(count - count2)
        
        



        