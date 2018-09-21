# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:28:01 2018

@author: rossc
"""

def isIn(char, aStr):
    
    y= int(len(aStr)//2)
    
    
    if len(aStr) ==0:
        return False
    elif len(aStr)==1:
        return char == aStr
    elif aStr[y] ==char:
        return True
    elif char > aStr[y]:
        return isIn(char, aStr[y+1:])
    elif char < aStr[y]:
        return isIn(char, aStr[:y])