def make_alternator(f, g):
    def h(n):
        i = 1
        while i <= n:
            if i % 2 == 0:
                print(g(i))
            else:
                print(f(i))
            i += 1
    return h


def cascade2(n):
    print(n)
    if n >= 10:
        cascade2(n//10)
        print(n)
