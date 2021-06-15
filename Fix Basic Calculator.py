def basic_calculator(a, o, b):
    if (o == "+"):                                                      # add
        return a + b
    elif (o == "-"):                                                    # subtract
        return a - b
    elif (o == "*"):                                                    # multiply
        return a * b
    elif (o == "/"):                                                    # divide
        return a / b
    elif (o != "/" or "-" or "+" or "*" or b == 0):
        return None

print(basic_calculator(3, '/', 0))                                       # Function calling and printing
