# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 11:38:58 2021

@author: Easin
"""

n,k = input().split()
n = int(n)
k = int(k)
if n%2 ==0:
    m = n//2
else:
    m = (n//2)+1
    
if k <= m:
    val = k+k-1
else:
    val = (k-m)*2
print(val)

'''    
list1 = []
list2 = []
#vals =list(range(1,n+1))
 
# 5(10-1) = 45
#1 3 5 7 9 2 4 6 8 10

#1 2 3 4 5 6 7 8 9 10
#odd: 1+2 = 3; 3+4 = 7; k+k-1
#even: (6-mid)*2, (7-mid)*2;( k-m)*2

for elem in range(len(vals)):
    if vals[elem] % 2 == 1:
        list1.append(vals[elem])
    elif vals[elem] % 2 == 0:
        list2.append(vals[elem])
final = list1+list2
#print(final)
print(final[k-1])
'''        