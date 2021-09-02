# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:32:11 2021

@author: Easin
"""

k,r = input().split()
k =int(k)
r = int(r)

n=1


while k*n % 10 !=0:
    if (k*n-r)%10 ==0:
        #print(n)
        break
    n+=1
print(n)