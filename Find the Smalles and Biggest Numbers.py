def min_max(nums):
    max = nums[0]                               # dummy variable to store max
    for i in nums:                              # looping elements
        if i > max:
            max = i                             # actual max
        else:
            continue
    min = nums[0]                               # dummy variable to store min
    for j in nums:                              # looping elements
        if j < min:
            min = j                             # actual min
        else:
            pass
    return min, max


print(min_max(min_max([7, 2, 3, 4, 5])))        # Function calling and printing
