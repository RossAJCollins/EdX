# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:19:01 2018

@author: rossc
"""
def polysum(n,s):
    import math
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter = (s*n)
    return round(area+perimeter**2,4)
