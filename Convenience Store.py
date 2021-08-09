def change_enough(change, amount_due):
    a = [None] * 4
    i = 0
    val = 0
    a[i] = int(change[i]) * 0.25
    i = i + 1
    a[i] = change[i] * 0.10
    i = i + 1
    a[i] = change[i] * 0.05
    i = i + 1
    a[i] = change[i] * 0.01
    for j in a:
        val = val + j
    return True if val > amount_due else False


print(change_enough([2, 100, 0, 0], 14.11))
