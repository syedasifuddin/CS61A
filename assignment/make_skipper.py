def make_skipper(k):
    def skip(n):
        i = 0
        while i <= n:
            if (i % k != 0):
                print(i)
            i += 1
    return skip
