# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:48:34 2021

@author: Easin
"""

in1 = input()

list1 = ["h","e","l","l","o"]
lis2 = [-1]
#if len(in1) <5:
#   print("NO")
    
 
if len(in1) >= 5:
    for elem in range(len(list1)):
      
        
        for val in range(len(in1)):
            if list1[elem] == in1[val] and val > lis2[-1]:
                lis2.append(val)
                break
            
                
if len(lis2) >= 6: 
    print("YES")
else:
    print("NO")