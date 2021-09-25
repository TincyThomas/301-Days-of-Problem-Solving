def prevent_distractions(txt):
    a = ["anime", "meme", "vines", "roasts", "Danny DeVito"]
    b = txt.split(" ")
    for i in b:
        if i in a:
            return "NO!"
    else:
        return "Safe watching!"


print(prevent_distractions("vins that butter my eggroll"))
