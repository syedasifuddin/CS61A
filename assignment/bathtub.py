def bathtub(n):
    def ducky_annihilator(rate):
        def ducky():
            nonlocal n
            nonlocal rate
            n = n - rate
            return n
        return ducky
    return ducky_annihilator


def weird_gen(x):
    if x % 2 == 0:
        yield x * 2
    else:
        yield x
        yield from weird_gen(x - 1)


def greeter(x):
    while x % 2 != 0:
        yield 'hello!'
        yield x
        print('goodbye!')
