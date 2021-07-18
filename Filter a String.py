def filter_string(txt):
    uc = 0                                                                                                                            # assiging 0
    ul = 0
    un = 0
    us = 0
    for i in txt:
        if i.isupper():                                                                                                               # Checking uppercase
            uc= uc +1
        elif i.islower():                                                                                                             # checking lowercase
            ul = ul + 1
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":    # Checking Number
            un = un + 1
        else:                                                                                                                         # this part works for special char
            us = us+1
    return [uc,ul,un,us]                                                                                                              # list of count of all
print(filter_string("**Airforce1**"))
