def possible_bonus(a, b):
    if b>a:                           # no bonus if enemy is below
        a =a +6                       # die can have only 1-6 values
        if a >= b:                    # a means i, i should score more than or equal to opponent
            return True
        else:
            return False
print(possible_bonus(3, 11))
