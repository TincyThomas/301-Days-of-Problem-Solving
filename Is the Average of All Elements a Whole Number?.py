def is_avg_whole(arr):
    a = 0
    for i in arr:
        a = a + i
    return True if a % len(arr) == 0 else False


print(is_avg_whole([1, 3,4]))
