# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:20:15 2018

@author: rossc
"""

def printMove(fr, to,move):
    print('Move No. ' + str(move) +'move from ' +str(fr) + ' to ' +str(to))
    
    
def Towers(n, fr, to, spare):
    moves = 0
    if n==1:
        moves+=1
        printMove(fr, to,moves)
    else:
        moves+=1
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare,to,fr)