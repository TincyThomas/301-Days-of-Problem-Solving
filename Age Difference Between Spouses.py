def age_difference(ages):
    ages.sort(reverse=True)                                 # sorting in DESC
    if ages[0]-ages[1] == 0:                                # taking difference of two greatest elements
        return "No age difference between spouses."
    elif ages[0]-ages[1] == 1:
        return "1 year"
    else:
        print(ages[0]-ages[1], end="")
        return " years"
print(age_difference([43, 85, 49, 86]))
