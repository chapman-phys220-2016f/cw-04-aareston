#!bin/usr/env python

import nose as n

"""
Implements midpoint integration rule.
"""

def midpoint(f,a,b,n):
    """
    Definition for midpoint integration rule

    Parameters
    ----------
        f: lambda
            function to be integrated
        a: float
            lower bound for integration
        b: float
            upper bound for integration
        n: int
            number of subintervals to use

    Returns
    -------
        S: float
            integral approximation
    """
    S = 0.0
    h = (b - a) / float(n)
    print h
    for i in range(n):
        S += h * f(a - 1 / 2 * h + i * h)
    return S

def test_midpoint():
    """
    Tests midpoint() for the case of f(x) = x^5, a = 0, b = 50, n = 50000
    """
    test = midpoint(lambda x: x ** 5, 0, 1, 50000)
    case = 0.2
    n.tools.assert_almost_equals(test, case)
