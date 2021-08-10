def determine_lever(l):
    count = -1
    for i in l:
        count = count +1
        if i == "f":
            if count ==1:
                return "first class lever"
            elif count == 2:
                return "second class lever"
            elif count ==0:
                return "third class lever"
print(determine_lever(["e", "f", "l"]))
