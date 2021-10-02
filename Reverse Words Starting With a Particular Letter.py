def special_reverse(s, c):
    qe = []
    qw = ""
    a = s.split(" ")
    for i in a:
        if i[0]==c:
            for j in i:
                qw = j + qw
            qe = qe + [qw]
            qw = ""
        else:
            qe = qe +[i]
    return " ".join(qe)
print(special_reverse("peter piper picked pickled peppers", "p"))
