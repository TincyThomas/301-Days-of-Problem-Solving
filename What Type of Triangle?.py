def get_triangle_type(lst):
    if len(lst)==3:
        a = set(lst)
        if len(a)==1:
            return "Equilateral"
        elif len(a) == 2:
            return "Isosceles"
        elif len(a)==3:
            return "Scalene"
    else:
        return "not a triangle"
print(get_triangle_type([2, 2, 2,4]))
