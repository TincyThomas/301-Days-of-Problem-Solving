def reverse(txt):
    t = ""
    for i in txt:
        if i.isupper():
            t= i.lower() + t
        elif i.islower():
            t= i.upper() + t
        else: t=i+t
    return t
print(reverse("Radar"))
