def validate_binary(b):
    parity = b[-1]
    a = b[0:len(b) - 1].count("1")
    if parity == "0":
        if a % 2 == 0:
            return True
    elif parity == "1":
        if a % 2!= 0:
            return False
        else:return True
    else:
        return False


print(validate_binary("11000001"))

