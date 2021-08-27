# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:10:43 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)


str1 = ""
for elem in range(in1):
    #print(elem)
    if (elem+1 != in1) and (elem+1) % 2 ==1:
        #print(elem+1)
        odd_n = "I hate that "
        str1 += odd_n
    elif (elem+1 != in1) and (elem+1) % 2 ==0:
        even_n = "I love that "
        str1 += even_n
    elif elem+1 == in1:
        if in1 % 2 ==1:
        #print(elem+1)
            odd_n = "I hate it"
            str1 += odd_n
        elif in1 % 2 ==0:
            even_n = "I love it"
            str1 += even_n
        
        
        
        
print(str1)

#I hate that I love that I hate it
    