# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:53:24 2021

@author: Easin
"""

in1 = input()
st1 = ""
flag = False

for val in range(1,len(in1)):
    
    if in1[val] == in1[val].lower():
        flag = True
if flag == False:
    for elem in range(len(in1)):
        #val = in1[elem]
        
        if in1[elem] != in1[elem].upper():
            st1 += in1[elem].upper()
        else:
            st1 += in1[elem].lower()
else:
    st1 = in1

print(st1)
        