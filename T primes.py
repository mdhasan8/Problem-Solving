# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:36:54 2021

@author: Easin
"""


in1 = input()
in1 = int(in1)
in2 = input().split()
list1 = []
for elem in range(len(in2)):
    list1.append(int(in2[elem]))
#print(list1)
import math
#print(dir(math))
def primenum(num):
    flag = True
    for vals in range(2,int(math.sqrt(num))+1):
        if num % vals == 0:
            flag = False
            break
    return flag        
         
for val in range(len(list1)):
    x = int(math.sqrt(list1[val]))
    #print(x)
    if list1[val] % 2 != 0  and x*x == list1[val] and list1[val]!=4 and list1[val] !=1 and primenum(x):
        print("YES")
    elif list1[val] == 4:
        print("YES")
    elif list1[val]==1:
        print("NO")
    else:
        print("NO")
        
    
        
        
        
        

                 
