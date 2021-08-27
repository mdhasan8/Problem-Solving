# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:47:58 2021

@author: Easin
"""

in1 = input()
in2 = input()
in3 = input()
'''
if len(in1) + len(in2) != len(in3):
    print("NO")
    
count = 0
for elem in range(len(in3)):
    for val in range(elem+1,len(in3)):
    
        if in3[elem] == in3[val]:
            count += 1
            break
print(count)

count1 = 0
for elem in range(len(in1)):
    for val in range(elem+1,len(in1)):
        if in1[elem] == in1[val]:
            count1 += 1
            break
print(count1)

count2 = 0
for elem in range(len(in2)):
    for val in range(elem+1,len(in2)):
        if in2[elem] == in2[val]:
            count2 += 1
            break
print(count2)
'''
import string
a_z = string.ascii_lowercase
a_z = a_z.upper()

flag = True
for val in range(len(a_z)):
    countf1 = 0
    for val2 in range(len(in3)):
        if a_z[val] == in3[val2]:
            countf1+=1
            #print(countf1)
            
    
    countf2 = 0        
    for val3 in range(len(in1)):
        if a_z[val] == in1[val3]:
            countf2+=1
    countf3 = 0        
    for val4 in range(len(in2)):
        if a_z[val] == in2[val4]:
            countf3+=1
            
    if countf1 != countf2 + countf3:
        flag = False
        break
    
    #print(countf1)
    #print(countf2)
    #print(countf3)

if flag == True:
    print("YES")
else:
    print("NO")         
        
            
    
    
    
    