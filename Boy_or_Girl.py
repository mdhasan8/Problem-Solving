# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 11:58:39 2021

@author: Easin
"""

in1 = input()
#print(len(in1))
count = 0

for elem in range(len(in1)):
    flag = True
    for val in range(elem+1,len(in1)):
        
        
        if in1[elem] == in1[val]:
            count = count
            flag = False
        
    if flag == True:
        count +=1
        
    
#print(count)
            
        
        
if count % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")