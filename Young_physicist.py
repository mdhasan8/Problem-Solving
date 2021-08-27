# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:42:10 2021

@author: Easin
"""

in1 = int(input())
list1 = []
for val in range(in1):
    in2 = input().split()
    #print(in2)
    list1.append(in2)
#print(list1)

'''
for elem in range(len(list1)-1):
    x = int(list1[elem][0]) + int(list1[elem+1][0]) + int(list1[elem+2][0]) 
    y = int(list1[elem][1]) + int(list1[elem+1][1]) + int(list1[elem+1][1]) 
    z = int(list1[elem][2]) + int(list1[elem+1][2]) + int(list1[elem+1][2]) 
    print(x)
    print(y)
    print(z)
    
'''
x =0
y = 0
z = 0
for elem in range(len(list1)):
    x += int(list1[elem][0])
    y += int(list1[elem][1])
    z += int(list1[elem][2])
    
if x ==0 and y ==0 and z ==0:
    print("YES")
else:
    print("NO")
    
    


