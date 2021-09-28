import math

def century_from_year(year):
    a  = []
    for i in str(year):
        a = a + [int(i)]
    if a [2] == 0 and a[3] ==0:
        return str(a[0])+str(a[1])
    else:
        q = str(a[0])+ str(a[1])
        w = int(q)
        w = w+1
        return w
print(century_from_year(2005))
