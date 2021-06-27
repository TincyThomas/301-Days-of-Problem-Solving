def yen_to_usd(yen):
    usd = yen / 107.5                           # conversion method
    usd = str(usd)                              # convert to string
    b = usd[0:4]                                # we need first three digits
    a = usd[4]                                  # cutting 3rd element
    if int(a)> 5:                               # checking 3rd element more than 5 or not
        return float(b)+0.01                    # str() needs to be converted to float() then do addition
    else:
        return float(b)                   
print(yen_to_usd(649))                          # function calling and printing
