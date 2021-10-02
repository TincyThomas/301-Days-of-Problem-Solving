def convert_binary(strin):
    import string
    val = ""
    qw = string.ascii_lowercase
    wq = string.ascii_uppercase
    fir = qw[0:13] + wq[0:13]
    sec = qw[13:] + wq[13:]
    for i in strin:
        if i in fir:
            val = val + "0"
        else:
            val = val + "1"
    return val


print(convert_binary("excLAIM"))
