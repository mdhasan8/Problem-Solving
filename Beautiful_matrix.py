# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:54:21 2021

@author: Easin
"""

in1 = input().split()
in2 = input().split()
in3 = input().split()
in4 = input().split()
in5 = input().split()

mat = [in1,in2,in3,in4,in5]
print(mat[0])

for elem in range(len(mat)):
    print("elem",elem)
    #print(mat[elem])
    for val in range(len(mat[0])):
        print("val",val)
        
        if mat[elem][val] == "1":
            
            swap = abs(2 - elem)
            swap1 = abs(2 - val)
            
            fin_swap = swap + swap1
print(fin_swap)            
        
    