from math import comb

def dbinom(x, n, p):
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))