def dna_to_rna(dna):
    a = []
    b = []
    count=0
    d = {"A":"U", "T":"A","G":"C","C":"G"}
    for i, j in d.items():
        a += [i]
        count+=1
    for k in dna:
        if k in a:
            b += [d[k]]
    return b
print(dna_to_rna("CGATATA"))
