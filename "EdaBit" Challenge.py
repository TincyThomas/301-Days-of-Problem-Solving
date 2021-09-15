def eda_bit(start, end):
    a =[]
    for i in range(start,end+1):
        if i%3==0 and i%5==0:
            a = a + ["Edabit"]
        elif i % 5 ==0:
            a = a +["Bit"]
        elif i % 3 == 0:
            a = a + ["Eda"]
        else:
            a= a + [i]
    return a
print(eda_bit(0, 10))
