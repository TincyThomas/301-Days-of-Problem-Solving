def get_decimal_places(n):
    try:
        count = 0
        for i in n:
            count = count + 1
            if i == ".":
                a = count
        return len(n) - a
    except:
        return "0"

print(get_decimal_places("400.2"))
