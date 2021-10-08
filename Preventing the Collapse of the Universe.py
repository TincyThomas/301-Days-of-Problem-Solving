def catch_zero_division(expr):
    try:
        c = eval(expr)
    except ZeroDivisionError:
        return True
    return False
print(catch_zero_division("2 / 1"))
