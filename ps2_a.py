#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Eric Hoppmann
"""

def pay_off_in_one_year_bisection(bal, apr):
    """
    This function computes the amount that needs to be paid every month in order
    to pay off a loan in 12 months. This function uses bisection search to find the
    solution within $0.01 

    :param float bal: Starting balance
    :param float apr: APR interest rate (expressed as a percentage, e.g. 10.5 indicates 
      10.5% / .105)
    :return: The number of months to pay off
    :rtype: int
    """
    return None

if __name__ == '__main__':
    bal = float(input('Enter the starting balance: '))
    apr = float(input('Enter the APR: '))
    monthly_payment = pay_off_in_one_year_bisection(bal, apr)
    print('Monthly Payment: ', monthly_payment)
