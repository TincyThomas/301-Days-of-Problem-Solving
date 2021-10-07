def parity_analysis(num):
    a = 0
    for i in str(num):
        a = a + int(i)
    return True if (a%2==0 and num%2==0) or (a%2!=0 and num%2!=0) else False
print(parity_analysis(12))
