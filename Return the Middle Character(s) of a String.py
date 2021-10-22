def get_middle(word):
    import math
    if len(word)%2==0:
        return word[int((len(word)/2)-1)] + word[int(len(word)/2)]
    else:
        return word[math.ceil(len(word)/2)-1]
print(get_middle("test"))
