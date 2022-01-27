def normalize(txt):
    if txt == txt.upper():
        return txt.capitalize() + "!"
    else:
        return txt


print(normalize("CAPaa LOCK DAY IS OVER"))
