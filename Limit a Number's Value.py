def limit_number(num, range_low, range_high):
    a = []
    for i in range(range_low,range_high+1):
        a = a +[i]
    if num in a:
        return num
    else:
        if num < range_low:
            return range_low
        else:
            return range_high
print(limit_number(12, 1, 10))
