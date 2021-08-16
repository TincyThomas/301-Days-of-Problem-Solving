def opposite_house(house, n):
    odd = []
    o = 1
    even = []
    e = 2
    for i in range(n):
        odd = odd + [o]
        o = o + 2
    for j in range(n):
        even = [e] + even
        e = e + 2
    if house in odd:
        a = odd.index(house)
        return even[a]
    elif house in even:
        b = even.index(house)
        return odd[b]
print(opposite_house(3, 5))
