def ink_levels(inks):
    a = []
    for key, value in inks.items():
        a = a+ [value]
    for k, v in inks.items():
        if v == min(a):
            return k
print(ink_levels({
  "cyan": 23,
  "magenta": 12,
  "yellow": 10
}))
