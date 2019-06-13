def pascal(row, column):
    if column == 0:
        return 1
    if column == row:
        return 1
    if column > row:
        return 0
    else:
        return pascal(row-1, column-1) + pascal(row-1, column)
