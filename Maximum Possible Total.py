def max_total(nums):
    b = []                                              # taking empty array
    for i in range(5):                                  # looping 5 times
        a = max(nums)                                   # taking max value from array
        b = b + [a]                                     # appending max value to new array
        nums.remove(max(nums))                          # deleting that max value from array
    c = 0                                               # initialization
    for j in b:                                         # looping list of 5 max values of old array
        c = c+j                                         # adding those 5 elements
    return c                                            # total sum


print(max_total([1, 1, 0, 1, 3, 10, 10, 10, 10, 1]))



