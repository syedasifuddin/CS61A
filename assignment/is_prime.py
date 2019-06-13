def is_prime(n):
    def prime_helper(n, i):
        if i == 0:
            return False
        if i == 1:
            return True
        elif n % i == 0:
            return False
        else:
            return prime_helper(n, i - 1)
    return prime_helper(n, n//2)
