def amazing_edabit(s):
    s = s.split(" ")                              # split input string to list
    f = "amazing."                                # check for substring
    a = s.index(f)                                # index of substring
    b = s[0:a]                                    # taking elements before of substring
    if "Edabit" in s:                             # if Edabit is present in input string
        return " ".join(s)                        # then do nothing
    else:
        s[a]="not amazing."                       # otherwise change it with not amazing
        return " ".join(s)                        # join list


print(amazing_edabit("Edabit is amazing."))
