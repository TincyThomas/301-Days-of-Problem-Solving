def relation_to_luke(name):
    a = {'Darth Vader': 'father', 'Leia': 'sister', 'Han': 'brother in law', 'R2D2': 'droid'}
    for p, r in a.items():
        if p == name:
            return "Luke, I am your " + r+ "."


print(relation_to_luke("Darth Vader"))
