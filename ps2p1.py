# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:38:48 2018

@author: rossc
"""
balance =484
annualInterestRate=0.2
monthlyPaymentRate=0.04
monthlyInterestRate = annualInterestRate/12.0

month=1

while month <=12:
    minimumPayment=monthlyPaymentRate*balance
    balance = round(balance - minimumPayment,2)
    balance = round(balance + (balance * monthlyInterestRate),2)

    month += 1

print("Remaining balance: ", balance)  