def km_to_miles(kilometers):
    a = kilometers * 0.621371                   # conversion formula
    b = str(a)                                  # making float string
    b = b[0:7]                                  # taking required 6 elements
    if int(b[6]) > 5:                           # checking if 6th element is more than 5 or not
        d = int(b[6]) + 1                       # if it is then add 1
        return float(b[0:6] + str(d))           # concatenating front 5 elements with computed d variable
    else:
        return float(b[0:7])


print(km_to_miles(8))
