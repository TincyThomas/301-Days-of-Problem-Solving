def is_prefix(word, prefix):
    return True if prefix[:len(prefix)-1] in word else False


def is_suffix(word, suffix):
    return True if suffix[1:] in word else False


print(is_suffix("vocation", "-logy"))
