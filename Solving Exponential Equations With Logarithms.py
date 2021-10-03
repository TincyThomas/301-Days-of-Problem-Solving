def solve_for_exp(a, b):
    x =1
    while True:
        if a ** x==b:
            return x
        else:
            x = x +1

print(solve_for_exp(9, 3486784401))
