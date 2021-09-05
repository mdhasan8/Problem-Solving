# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:32:20 2021

@author: Easin
"""

t = input()
t = int(t)
for elem in range(t):

    in1 = input()
    in1 = int(in1)
    
    x = in1//2
    if x%2 !=0:
        print("NO")
    else:
        #2+4+6+....+x
        #2(1+2+3+.....+x//2)
        num =2
        sum1 = 0
        even= []
        while in1 >= num:
            sum1 = sum1 + num 
            even.append(num)
            num = num+2
        #print("sum",sum1)
        #print(even)
            
        odd = []
        num1=1
        #sum2 = 0
        while sum1 - num1 < sum1 and sum1 > num1:
            sum1 = sum1 -num1
            odd.append(num1)
            num1 = num1 +2
        odd[-1] = odd[-1] +sum1
        #print(odd)
        final = even + odd
        print("YES")
        #print(final)
        for val in range(len(final)):
            print(final[val])
    
        
    
    
    