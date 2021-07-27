def binary_to_decimal(lst):
    a = len(lst)                                                  # a contains length of list
    b = []                                                        # b denotes empty list
    d = 0                                                         # assign d with 0
    count = -1                                                    # assign count equals -1
    for i in range(a):                                            # loop length of input list
        b = [2**i] + b                                            # make a list of elements raised with increasing power of 2
    for j in lst:                                                 # looping elements od input list
        count = count + 1                                         # everytime increase count by 1...this is for finding index 
        if j == 1:                                                # check when input is 1
            d = d+b[count]                                        # add that index value
    return d                                                      # total sum whereever it got 1 in the input list

print(binary_to_decimal([1, 1, 1, 1, 1, 0, 1, 1, 0, 1]))
