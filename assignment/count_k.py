def count_k(n, k):
    # we can take up to and including k steps at a time
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total
