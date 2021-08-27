# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:04:44 2021

@author: Easin
"""

input1 = input()
input2 = input()
input1 = input1.lower()
input2 = input2.lower()
#print(input1)
#print(input2)

for elm in range(len(input1)):
    if input1[elm] == input2[elm]:
        
        continue
        
        
    elif input1[elm] > input2[elm]:
        print("1")
        break
        
    elif input1[elm] < input2[elm]:
        print("-1")
        break

if input1 == input2:
    print("0")

    
        
    
    
