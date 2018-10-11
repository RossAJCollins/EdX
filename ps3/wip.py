# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:50:53 2018

@author: rossc
"""


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in secretWord.lower():
        val=False
        if x in lettersGuessed:
           val=True
        else:
            val=False
            break
    return val

def getGuessedWord(secretWord, lettersGuessed):
    a=""
    for x in secretWord.lower():
        if x in lettersGuessed:
            a= a + x
        else:
            a=a+'_'
    return a


def getAvailableLetters(lettersGuessed):
    import string
    alpha = string.ascii_lowercase
    a=""
    alphaList=[]
    for y in alpha:
        alphaList.append(y)

    for x in lettersGuessed:
        if str(x).lower() in alpha:
            alphaList.remove(x)
    for z in alphaList:
        a = a +str(z)
    return a
