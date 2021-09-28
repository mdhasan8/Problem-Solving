# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:28:47 2021

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
    
    count_odd = 0
    count_even = 0
    for val in range(len(list1)):
        if (val % 2 ==0) and list1[val] % 2 !=0:
            count_odd += 1
        if (val % 2 !=0) and list1[val] % 2 ==0:
            count_even += 1
    #print(count_even)
    #print(count_odd)
    
    if count_even != count_odd:
        print(-1)
    else:
        print(count_even)
        

        
    
