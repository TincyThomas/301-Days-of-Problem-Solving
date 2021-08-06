def darts_scoring(x, y):
    b= [x,y]
    for i in b:
        if i >10:
            return 0
        elif 10 >= i > 5:
            return 1
        elif 5 >= i > 1:
            return 5
        elif i<=1:
            return 10
print(darts_scoring(0, 0))
