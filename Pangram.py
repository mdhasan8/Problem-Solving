# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:12:15 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input()

import string
a_z = string.ascii_lowercase

in2 = in2.lower()
#print(in2)
#flag = False
for elem in range(len(a_z)):
    
    for val in range(len(in2)):
        if a_z[elem] == in2[val]:
            flag = True
            break
        else:
            flag = False
    if flag == False:
        break
            
            

if flag == True:
    print("YES")
else:
    print("NO")
    