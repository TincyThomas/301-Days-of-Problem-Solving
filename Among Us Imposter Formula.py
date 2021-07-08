def imposter_formula(i, p):
    a = (i / p) * 100               # given formula
    w = str(a)                      # making it stirng
    b = int(w[3])                   # takeing only 3rd element
    if b >5:                        # checking if it is greater or smaller
        return a + 0.5              # add 0.5
    else:
        return int(a)               # otherwise return its int 



print(imposter_formula(1,8))
