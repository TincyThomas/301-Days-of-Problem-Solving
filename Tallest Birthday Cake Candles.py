def birthday_cake_candles(candles):
    a = candles[0]                                    # Dummy variable to store first value of list
    for i in candles:                                 # loop to take all elements of i
        if a <i:                                      # check a lesser than current looped element or not
            a = i                                     # if a is lesser then assign i's value to a
        else:
            pass                                      # otherwise do nothing
    return candles.count(a)                           # refering to list of values in candles, then counting the times of the maximum value


print(birthday_cake_candles([4, 7, 7, 7]))            # function printing and calling
