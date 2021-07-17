def highest_digit(num):
    a =[]                               # empty list
    while num>0:                        # looping as input more than zero
        n = num % 10                    # taking last digit in n
        a = [n] + a                     # putting into lisy
        num = int(num/10)               # stripping off last digit everytime
        continue
    return max(a)                       # max() works on list only
print(highest_digit(379))
