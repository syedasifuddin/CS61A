def count_stair_ways(n):
    # n is the number of stairs
    # we can either go one step or two steps in a row
    # total number of ways we can go up
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return count_stair_ways(n-2) + count_stair_ways(n-1)
