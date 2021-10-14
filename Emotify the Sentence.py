def emotify(txt):
    d = {"smile":":D","grin":":)","sad":":(","mad":":P"}
    tx = txt[8:]
    return txt[:8] + d[tx]
print(emotify("Make me grin"))
