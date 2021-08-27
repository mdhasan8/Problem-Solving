# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:00:12 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

list1 = []
for elem in range(in1):
    in2 = input()

    if in2 not in list1:
        print("OK")
    else:
        count = list1.count(in2)
        
        var = in2+ (str(count))
        '''
        while var in list1:
            
            count += 1
            var = in2+ (str(count))
        '''    
        #in2 = var
        print(var)
    list1.append(in2)
#print(list1)

    
    