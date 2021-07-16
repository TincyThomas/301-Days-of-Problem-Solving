def add_nums(nums):
    a =0                                # initialisation
    nums = nums.split(",")              # split with comma
    for i in nums:                      # loop list
        a =a + int(i)                   # adding numbers
    return a                            # total sum
print(add_nums("2, 5, 1, 8, 4"))
