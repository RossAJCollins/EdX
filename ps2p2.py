# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:23:25 2018

@author: rossc
"""

balance = 3926.00
annualInterestRate = 0.2


monthlyInterest = annualInterestRate/12.0

for payment in range(10.0,3926.00,0.01):
    wbalance = balance
    month =1    
    while month <=12:
        wbalance = wbalance-payment
        wbalance = round(wbalance +(wbalance*monthlyInterest),2)
        month +=1
    if wbalance <=0:
        break
print("Lowest Payment: ", payment)