def NOT(num):
    return 0 if num == 1 else 1                                     # not reverses input


def AND(num, num2):
    return 1 if (num == 1) and (num2 == 1) else 0                   # and is true when all inputs are 1


def OR(num, num2):
    return 0 if (num == 0) and (num2 == 0) else 1                   # or is false only when all inputs are 0


print(NOT( 0))                                                      # Function calling and printing
