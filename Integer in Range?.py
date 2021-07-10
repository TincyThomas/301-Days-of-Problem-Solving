def int_within_bounds(n, lower, upper):
    if type(n) == int:                      # when type equals int
        for i in range(lower, upper):       # looping through given range 
            if n == i:                      # when input equals number within range
                return True
    else:
        return False


print(int_within_bounds(4, 2, 8))

