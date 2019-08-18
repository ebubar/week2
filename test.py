import pytest
import basic_test
import lab2a
import lab2b


def test_basic_test():
    for i in [-1000, 0, 1000]:
        assert basic_test.return_n(i) == i

def test_lab2a_1():
    assert lab2a.months_to_pay_off(5000, 18, 100) == 86


def test_lab2a_2():
    assert lab2a.months_to_pay_off(25000, 1, 1000) == 26


def test_lab2a_3():
    assert lab2a.months_to_pay_off(100000, 1.5, 1000) == 107


def test_lab2b_1():
    assert lab2b.pay_off_in_one_year_simple(5000, 18) == 460


def test_lab2b_2():
    assert lab2b.pay_off_in_one_year_simple(25000, 1.5) == 2110


def test_lab2b_3():
    assert lab2b.pay_off_in_one_year_simple(50000, 25) == 4700
