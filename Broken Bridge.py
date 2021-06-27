def is_safe_bridge(s):
    for i in s:
        if i==" ":                          # space in between indicates broken bridge
            return False
        else:
            continue
    return True
print(is_safe_bridge("######"))             # Function calling and printing
