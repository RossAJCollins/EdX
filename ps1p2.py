# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:37:44 2018

@author: RossA
"""

s = input('A bloody string: ')
count = 0

for x in range(0, (len(s))-2):
    codon = s[x:x+3]
    if codon == 'bob':
        count = count +1

count = str(count)
print("Number of times bob occurs is: " + count)