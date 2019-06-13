from operator import add, mul


def combine(n, f, result):
    if n == 0:
        return result
    else:
        return combine(n//10, f, f(n % 10, result))
