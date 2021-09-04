def alphabet_soup(txt):
    a = []
    for i in txt:
        a = a + [i]
    a.sort()
    return a

print(alphabet_soup("hacker"))

