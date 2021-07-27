def is_in_range(n, r):
    for v in range(r["min"], r["max"]):
        if n == v:
            return True
        else:
            return False


print(is_in_range(2, {"min": 4, "max": 5}))
