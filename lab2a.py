#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Eric Hoppmann
"""

def months_to_pay_off(bal, apr, min_pmt):
    """
    This function computes the number of months required to pay off a loan by making the 
    minimum payment every month.

    :param float bal: Starting balance
    :param float apr: APR interest rate (expressed as a percentage, e.g. 10.5 indicates 
      10.5% / .105)
    :param float min_pmt: Minimum payment
    :return: The number of months to pay off
    :rtype: int
    """
    apr /= 100
    monthly_rate = (1 + apr) ** (1 / 12) - 1
    months = 0

    while bal > 0:
        bal += bal * monthly_rate
        bal -= min_pmt
        months += 1

    return months

if __name__ == '__main__':  # This means that this code only runs when the file is run by python, not when imported as a module
    bal = float(input('Enter the starting balance: '))
    apr = float(input('Enter the APR as a percentage: '))
    min_pmt = float(input('Enter the monthly payment: '))
    months = months_to_pay_off(bal, apr, min_pmt)
    print('Months to pay off: ', months)
