def filter_state_names(lst, cat):
    a = []
    for i in lst:
        if cat == "abb":
            if i.isupper()==True:
                a = a+[i]
    for i in lst:
        if cat == "full":
            if i.isupper() == False:
                a = a + [i]
    return a
print(filter_state_names(["Arizona", "CA", "NY", "Nevada"], "abb"))
