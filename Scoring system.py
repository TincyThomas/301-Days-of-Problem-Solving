def calculate_scores(txt):
    return [txt.count("A"),txt.count("B"),txt.count("C")]                     # list containing count of required variables in required order


print(calculate_scores("C"))
