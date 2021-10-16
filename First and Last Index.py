def char_index(word, char):
    l = len(word)
    a = word.index(char)
    re = word[::-1]
    b = re.index(char)
    return [a,l-(b+1)]
print(char_index("hello", "l"))
