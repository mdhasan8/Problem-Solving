# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:34:15 2021

@author: Easin
"""

s,n = input().split()
s = int(s)
n = int(n)

dict1 = []
for elem in range(n):
    dict1.append(input().split())
    
    
#print(dict1)
#dict1.sort()
#print(dict1)
    
for val in range(len(dict1)):
    
    #for val2 in range(len(dict1)):
    dict1[val][0] = int(dict1[val][0])
    dict1[val][1] = int(dict1[val][1])
#print(dict1)
dict1.sort()
#print(dict1) 

for val in range(len(dict1)-1):
    
    #for val2 in range(len(dict1)-1):
    if s > dict1[val][0]:
        s = s + dict1[val][1]
          
if s > dict1[-1][0]:
    print("YES")
else:
    print("NO")
            

  
    