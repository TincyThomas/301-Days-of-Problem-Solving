def left_digit(num):
    n = [str(i) for i in range(10)]
    for i in num:
        if i in n:
            return i
print(left_digit("TrAdE2W1n95!"))
