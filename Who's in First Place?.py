def first_place(road):
    for i in range(len(road)-1,0,-1):           # looping in reverse manner
        if road[i]!= "=":                       # checking element equal to "="
            return road[i]                      # when not equal print character
        else:
            continue
print(first_place("prog=re=s=s="))
