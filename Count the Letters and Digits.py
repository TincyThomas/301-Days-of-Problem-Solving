def count_all(txt):
    count = 0
    dig = 0
    for i in txt:
        if i.isalpha():
            count = count +1
        else:
            dig = dig +1
    return "{"+ "LETTERS: " +str(count) + ", DIGITS: "+ str(dig)+"}"
print(count_all("Hello World"))
