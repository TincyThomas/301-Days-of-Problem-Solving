def word(s):
    a = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}          # making dictionary
    for key, value in a.items():                                                                                                # looping key and value 
        if key==s:                                                                                                              # when key equals s
            return value                                                                                                        # return its value pair


print(word("nine"))
