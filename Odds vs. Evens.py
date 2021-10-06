def odds_vs_evens(num):
    a = str(num)
    even = 0
    q = []
    odd = 0
    for i in a:
        q = q + [int(i)]
    for j in q:
        if j % 2 == 0:
            even = j + even
        else:
            odd = j + odd
    if even > odd:
        return "even"
    elif odd > even:
        return "odd"
    else:
        return "equal"


print(odds_vs_evens(54870))
