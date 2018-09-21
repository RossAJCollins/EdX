# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:34:12 2018
"""

balance = 999999
annualInterestRate =0.18

monthlyInterestRate = annualInterestRate /12.0
epsilon = 0.50
result = balance
def calculate(payment):
    month=1
    wBalance = balance
    while month <=12:
        wBalance = round(wBalance - payment,2)
        wBalance = round(wBalance+wBalance * monthlyInterestRate,2)
        month +=1
    return wBalance
        




upper = (balance *(1+monthlyInterestRate)**12)/12
lower = balance/12.0


while abs(result) > epsilon :
    guess = (upper+lower)/2.00
    result=(calculate(guess))
    if result > 0:
        lower = guess
    elif result < 0:
        upper = guess

print("Lowest Payment: ",round(guess,2))


    