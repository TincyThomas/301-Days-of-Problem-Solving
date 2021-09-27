def asc_des_none(lst, s):
    b =[]
    if s == "None":
        return lst
    lst.sort()
    if s == "Asc":
        return lst
    else:
        for i in lst:
            b = [i] + b
        return b
print(asc_des_none([4, 5, 2, 1], "Dsc" ))
