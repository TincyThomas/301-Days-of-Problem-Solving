def can_capture(rooks):
    if rooks[0][0] == rooks[1][0]:
        return True
    elif rooks[0][1] == rooks[1][1]:
        return True
    else:
        return False


print(can_capture(["A7", "E8"]))
