#!bin/usr/env python

import numpy as np
import matplotlib.pyplot as plt

"""
Implements 5 different mathematical sequences which converge to pi.
Plots them simultaneously to determine which converges fastest
"""

def a_n(n):
    """
    First sequence of partial sums converging to pi.

    Parameters
    ----------
        n: int
            number of terms to use in approximation

    Returns
    -------
        terms: np.array
            sequence of partial sums approximating pi
    """
    terms = np.zeros(n)
    S = 0
    for i in range(1, n + 1):
        S += 4.0 * (-1) ** (i + 1) / (2 * i - 1)
        terms[i - 1] = S
    return terms

def b_n(n):
    """

    """
    terms = np.zeros(n)
    sums = np.zeros(n)
    S = 0.0
    for i in range(1, n + 1):
        terms[i - 1] = 6.0 * i ** (-2) 
        sums[i - 1] = np.sqrt(np.sum(terms[0:i]))
    return sums

def c_n(n):
    """

    """
    terms = np.zeros(n)
    sums = np.zeros(n)
    S = 0.0
    for i in range(1, n + 1):
        terms[i - 1] = 90.0 * i ** (-4)
        sums[i - 1] = np.power(np.sum(terms[0:i]), 0.25)
    return sums

def d_n(n):
    """

    """
    terms = np.zeros(n)
    S = 0.0
    for i in range(n):
        S += 6.0 / np.sqrt(3) * (-1) ** i / (3 ** i * (2 * i + 1))
        terms [i] = S
    return terms

def e_n(n):
    """

    """
    terms = np.zeros(n)
    S = 0.0
    for i in range(n):
        S += 16.0 * (-1) ** i / (5 ** (2 * i + 1) *(2 * i + 1)) - 4.00 * (-1) ** i / (239 ** (2 * i + 1) * (2 * i + 1))
        terms[i] = S
    return terms

def a_eq(x,y,eps = 1E-5):
    return (abs(x - y) < eps)

def test_a_n():
    """
    Tests a_n() for the case of 2 terms
    """
    test = a_n(2)
    case = [4.0, 2.66666]
    success = 0
    for (a,b) in zip(test,case):
        if a_eq(a,b):
            success += 1
    assert (success == 2)

def test_b_n():
    """
    Tests b_n() for the case of 2 terms
    """
    test = b_n(2)
    case = [2.44948974,2.73861278]
    success = 0
    for (a,b) in zip(test,case):
        if a_eq(a,b):
            success += 1
    assert (success == 2)

def test_c_n():
    """
    Tests c_n() for the case of 2 terms
    """
    test = c_n(2)
    case = [3.08007028, 3.12710786]
    success = 0
    for (a,b) in zip(test,case):
        if a_eq(a,b):
            success += 1
    assert (success == 2)

def test_d_n():
    """
    Tests d_n() for the case of 2 terms
    """
    test = d_n(2)
    case = [3.46410161,3.07920143]
    success = 0
    for (a,b) in zip(test,case):
        if a_eq(a,b):
            success += 1
    assert (success == 2)

def test_e_n():
    """
    Tests e_n() for the case of 2 terms
    """
    test = e_n(2)
    case = [3.18326359,3.14059702]
    success = 0
    for (a,b) in zip(test,case):
        if a_eq(a,b):
            success += 1
    assert (success == 2)

#--------------------------------------------------------------------------------------------------------------------#

def main():
    plot_sequences()

def plot_sequences():
    n = 5
    x = np.arange(5)
    plt.plot(x, np.squeeze(a_n(n)), 'r')
    plt.plot(x, np.squeeze(b_n(n)), 'g')
    plt.plot(x, np.squeeze(c_n(n)), 'b')
    plt.plot(x, np.squeeze(d_n(n)), 'c')
    plt.plot(x, np.squeeze(e_n(n)), 'm')

def test_plot():
    print len(range(32))
    print a_n(32).size
    assert len(range(32)) == a_n(32).size

if __name__ == "__main__":
    main()
