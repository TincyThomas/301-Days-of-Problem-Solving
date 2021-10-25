def malthusian(food_growth, pop_mult):
    food = 100
    pop = 100
    count = -1
    while True:
        count = count + 1
        #print(pop,food,count)
        if pop<=food:
            food = food+food_growth
            pop = pop*pop_mult
        elif pop>food:
            return count
        else:
            continue
print(malthusian(5879, 1.77))
