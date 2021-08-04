def calculate_years(human_years):
    if human_years == 1:
        return [human_years, 15, 15]
    elif human_years == 2:
        return [human_years, 24, 24]
    elif human_years > 2:
        while (True):
            cat = 24
            dog = 24
            for i in range(human_years - 2):
                cat = cat + 4
                dog = dog + 5
            return [human_years, cat, dog]


print(calculate_years(10))
