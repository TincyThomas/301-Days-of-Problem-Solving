def flip_end_chars(txt):
    if len(txt) < 2:
        return "Incompatible."
    if type(txt)!=str:
        return "Incompatible."
    if txt[0]==txt[-1]:
        return "Two's a pair."
    else:
        return txt[-1]+txt[1:len(txt)-1]+txt[0]
print(flip_end_chars("z"))
