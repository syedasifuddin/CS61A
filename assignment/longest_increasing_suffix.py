def longest_increasing_suffix(n):
    m,suffix,k = 10,0,1
    suffix = n % 10
    n = n // 10
    while n:
        n, last = n // 10, n % 10
        if suffix // k > last:
            m, suffix, k = m * 10 , last * m + suffix, 10*k
        else:
            return suffix
    return suffix
    
longest_increasing_suffix(63134)
longest_increasing_suffix(233)
longest_increasing_suffix(5689)
longest_increasing_suffix(568901)



a = [1,2,3,4,5]
mainlist = []
dict = {}
count = 1
for i in range(len(a)):
    if (fn(a[i],a[i+1]) < 0.5):
        dict[count + 1] = [a[i+1]]
    else:
        dict[count] = []


