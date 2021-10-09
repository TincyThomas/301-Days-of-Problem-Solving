def sort_descending(num):
    a = []
    q = ""
    for i in str(num):
        a = a + [int(i)]
    a.sort(reverse = True)
    for j in a:
        q = q+str(j)
    return q
print(sort_descending(1254859723))
