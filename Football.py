# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:06:01 2021

@author: Easin
"""

in1 = input()
count = 1

for elem in range(len(in1)-1):
    if in1[elem] == in1[elem+1]:
            count = count+1
    else:
        count = 1
    if count ==7:break
    
if count >=7:
    print("YES")
elif count !=7:
    print("NO")
    
        