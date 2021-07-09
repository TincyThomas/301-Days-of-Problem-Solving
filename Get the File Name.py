def get_filename(path):
    s = ""                                        # intialisation
    a  = ""                                       # initialisation
    for name in range(len(path)-1,0,-1):          # reverse looping
        if path[name]=="/":                       # when char meets slash
            for i in s:                           # taking reverse string making it straight
                a = i+a
            return a                              # final folder name
        else:
            s = s + path[name]                    # taking char of folder name
print(get_filename("C:/Projects/pil_tests/ascii/edabit.txt"))
