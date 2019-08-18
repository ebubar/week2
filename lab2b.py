#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Eric Hoppmann
"""


def pay_off_in_one_year_simple(bal, apr):
    """
    This function computes the amount that needs to be paid every month in order
    to pay off a loan in 12 months. This function only searches in multiples of $10. 

    :param float bal: Starting balance
    :param float apr: APR interest rate (expressed as a percentage, e.g. 10.5 indicates 
      10.5% / .105)
    :return: The number of months to pay off
    :rtype: int
    """
    apr /= 100
    monthly_rate = (1 + apr) ** (1 / 12) - 1
    monthly_payment_increment = 10
    monthly_payment = monthly_payment_increment

    while True:
        bal_at_end = bal
        for i in range(12):
            bal_at_end += bal_at_end * monthly_rate
            bal_at_end -= monthly_payment
        if bal_at_end <= 0:
            break
        else:
            monthly_payment += monthly_payment_increment

    return monthly_payment


if __name__ == '__main__':
    bal = float(input('Enter the starting balance: '))
    apr = float(input('Enter the APR: '))
    monthly_payment = pay_off_in_one_year_simple(bal, apr)
    print('Monthly Payment: ', monthly_payment)
