def clean_up_list(lst): 
    a = []                                        # assigning variable a to be a list
    b = []                                        # assigning variable b to be a list
    for i in lst:                                 # looping elements of i
        i=int(i)                                  # converting str i to integer using built-in function
        if i % 2 == 0:                            # checking whether i is even or not
            a = a + [i]                           # if even add that i's value to variable a
        else:
            b = b + [i]                           # seems it is odd, so add to variable b
    return [a]+[b]                                # returns two separate list of a and b with even and odd numbers respectively


print(clean_up_list(["9", "4", "5", "8"]))        # Function calling and printing
