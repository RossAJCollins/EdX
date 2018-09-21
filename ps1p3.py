# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s=input("string :")
longest =""
for x in range(len(s)-1):
    slice =""
    y=x+1
    while y <=len(s):
        prev_slice = slice
        slice = s[x:y]
        if slice[len(slice)-2] > slice[len(slice)-1]:
            break
        elif y == len(s):
            prev_slice=slice
            break
        else:
            y +=1
    if len(prev_slice) > len(longest):
        longest=prev_slice


print("Longest substring in alphbetical order2is: "+longest)