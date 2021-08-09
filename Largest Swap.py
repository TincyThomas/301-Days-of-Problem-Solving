def largest_swap(num):
    a = ""
    for i in str(num):
        a = i+a
    return True if num>int(a) else False
print(largest_swap(27))
