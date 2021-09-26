def is_vowel_sandwich(s):
    vow = ["a","e","i","o","u"]
    if len(s) == 3:
        if s[1] in vow:
            if (s[0] not in vow and s[2] not in vow ):
                return True
            else:
                return False


print(is_vowel_sandwich("bat"))
