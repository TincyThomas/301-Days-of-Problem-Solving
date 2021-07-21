def num_to_dict(lst):
    import string
    a = string.ascii_lowercase
    a = list(a)
    j = 0
    b={}
    ma = {}
    mai = []
    for i in range(97,123):
        b[i]=a[j]
        j = j+1
    for key,value in b.items():
        for l in lst:
            if l==key:
                ma[key]=value
    mai.append(ma)
    return mai
print(num_to_dict([118, 117, 120]))
