# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:46:46 2021

@author: Easin
"""

in1 = input()
#flag = True
for elem in range(len(in1)):
    if in1[elem] == "H" or in1[elem] == "Q" or in1[elem] == "9":
        flag = False
        break
    else:
        flag = True
if flag == False:
    print("YES")
else:
    print("NO")
    
