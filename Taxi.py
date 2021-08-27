# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 11:27:57 2021

@author: Easin
"""

in1 = input()
in1 = int(in1)

in2 = input().split()
list1 = []
for val in range(in1):
    input2 = int(in2[val])
    list1.append(input2)
    
#print(list1)
'''
total = 0
for elem in range(len(list1)-1):
    for val2 in range(len(list1)):
        if list1[elem] == 1 and list1[val2] == 3:
            one_thr = list1[elem] + list1[val2]
            total += one_thr
        elif list1[elem] == 1 and list1[val2] != 3:
        
            
        if list1[elem] == 2 and list1[val2] == 2:
            two_two = list1[elem] + list1[val2]
print(one_thr)    
print(two_two) 
'''

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for elem in range(len(list1)):
    if list1[elem] == 1:
        count_1 += 1
    if list1[elem] == 2:
        count_2 += 1
    if list1[elem] == 3:
        count_3 += 1
    if list1[elem] == 4:
        count_4 += 1
#print(count_1)
#print(count_2)
#print(count_3)
#print(count_4)

car = 0

car = car + count_4
car = car + count_3


#if count_1 == count_3:
#    count_13 = count_1*1 + count_3*3
    
extra_1 = 0
extra_2 = 0    
if count_1 > count_3:
    count_11 = count_1 - count_3
    extra_1 = count_11*1
    #count_13 = count_3*1 + count_3*3
    
#elif count_1 < count_3:
#    count_33 = count_3 - count_1
#    extra_3 = count_33*3
#    count_13 = count_1*1 + count_1*3
            
    
if count_2%2 == 0:
    car_count2 = (count_2*2) // 4
    car = car + car_count2

if count_2%2 == 1:
    car_count2 = (count_2*2) // 4
    car = car + car_count2
    extra_2 = 2

extra = extra_1 + extra_2
if extra % 4 == 0:
    car = car + extra//4
if extra % 4 != 0:
    car = car + extra//4+1
print(car)
          
    