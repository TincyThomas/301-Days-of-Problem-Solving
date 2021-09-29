def halloween(dt):
    a = str(dt)
    if a[4:] == "/10/31":
        return "Bonfire toffee"
    else:
        return "toffee"
print(halloween("2013/10/31"))
