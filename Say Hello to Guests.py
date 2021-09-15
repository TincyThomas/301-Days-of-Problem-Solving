def greet_people(names):
    a = ""
    for i in names:
        a = a + "Hello "+ i + ","
    return a
print(greet_people(["Frank", "Angela", "Joe"]))
