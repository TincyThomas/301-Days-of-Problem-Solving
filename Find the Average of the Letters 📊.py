def average_index(letters):
    import string                         
    s = string.ascii_lowercase
    a =list(s)                                  # making list of alphabets
    d = {}                                      # empty dictionary
    l = 1                                       # assignment
    for k in a:                                 # loop through alphabets
        d[k] = l                                # filling dictionary
        l = l+1                                 # incrementing value location
    an =0                                       # assignment
    for key,value in d.items():                 # looping key value of d
        for le in letters:                      # looping input
            if key==le:                         # when input matches
                an = an +value                  # use its value
    return round(an/len(letters),2)
print(average_index(["y", "o", "u", "a", "r", "e", "t", "h", "e", "b", "e", "s", "t"]))
	
