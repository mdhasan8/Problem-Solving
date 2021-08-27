# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:22:27 2021

@author: Easin
"""

in1 = input()
x = ""
'''
for elem in range(len(in1)-3):
    if in1[elem:elem+3] == "WUB":
        x = x+in1[elem+4]
    print(in1[elem:elem+3])
print(x)
'''
elem = 0
while elem < len(in1)-3:
    if in1[elem:elem+3] == "WUB":
        x = x + " "
        elem = elem +2
    else:
        x =x + in1[elem] 
    elem += 1

if in1[elem:elem+3] != "WUB":
    x = x + in1[elem:elem+3]
print(x)
        
    
    
        