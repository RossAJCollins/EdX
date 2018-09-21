# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:20:44 2018

@author: rossc
"""

rossHandle = open('test','w')


for i in range(2):
    name = input('Enter name: ')
    rossHandle.write(name + '\n')
rossHandle.close()