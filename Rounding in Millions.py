def millions_rounding(lst):
    a = []
    for i in lst:
        i[1] = int(round(i[1],-6))
        a = a+[i]
    return a
print(millions_rounding([
  ["Nice", 942208],
  ["Abu Dhabi", 1482816],
  ["Naples", 2186853],
  ["Vatican City", 572]
]))
