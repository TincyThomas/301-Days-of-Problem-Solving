def card_hide(card):
    l= len(card)-4
    a = ""
    for i in range(-1,-5,-1):
        a = card[i] + a
    return ("*" * l) + a
print(card_hide("1234123456785678"))
