# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:11:04 2021

@author: Easin
"""

k,n,w = input().split()
k = int(k)
n = int(n)
w = int(w)
i = 0
for val in range(w+1):
    i += val
#print(i)
    
#i = [*range(1,w+1,1)]
total = k*i
#total = k*sum(i)
loan = total -n
#print(loan)

if n > total:
    print("0")
else:
    print(loan)