def add_this_many(x, el, lst):
    for i in lst:
        if i == x:
            lst.append(el)
    return lst
