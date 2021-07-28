def test_jackpot(result):
    t = 0                                     # for taking index
    for i in range(3):                        # we know size of input list is 4 always so taking minus 1 of it
        if result[i]==result[i+1]:            # checking alternate indexes
            t = t+1                           # incrementing index value by 1
            if t==3:                          # i.e. all elements seem same
                return True                   # finally true
    else:
        return False                          # simpyy lets get out and print False if things don't go the same way
print(test_jackpot(["@", "@", "@", "["]))
