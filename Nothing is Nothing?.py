def nothing_is_nothing(*args):
    l=list(args)                                                                            # make a list of elements of input
    for i in l:                                                                             # loop list
        if i ==0 or i == False or i == None or i == {} or i == [] or i== ():                # checking for required elements
            return False                                                                    # when found return False
    return True


print(nothing_is_nothing(0, False, [], {}))
