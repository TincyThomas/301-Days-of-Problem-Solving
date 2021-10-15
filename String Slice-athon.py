def challenge1(s):
    return s[:5]

def challenge2(s):
    return s[-5:]

def challenge3(s):
    return s[::-1]

def challenge4(s):
    return s[5::-1]

def challenge5(s):
    return "".join([i for i in s[-7:] if s.index(i) %2!=0])

print(challenge5("abcdefghijklmnopqrstuvwxyz"))
