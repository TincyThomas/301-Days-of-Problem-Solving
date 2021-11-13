def get_number_of_apples(n, p):
    a = n-((int(p[:-1])/100)*n)
    if a == 0:
        return "The children didn't get any apples"
    else:
        return int(a)
print(get_number_of_apples(10, "90%"))
