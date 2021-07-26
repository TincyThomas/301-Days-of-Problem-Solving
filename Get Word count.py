def count_words(txt):
    count = 1
    for i in txt:
        if i == " ":
            count = count + 1
    return count
print(count_words("This is a test"))
