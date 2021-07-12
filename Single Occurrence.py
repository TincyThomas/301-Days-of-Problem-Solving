def single_occurrence(txt):
    st = txt.upper()
    for char in st:
        a = st.count(char)
        if a == 1:
            return char.upper()
print(single_occurrence("AAAAVNNNNSS"))
