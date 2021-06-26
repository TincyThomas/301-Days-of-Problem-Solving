def create_id(firstname, lastname):
    for i in firstname:                                 # looping char in firstname             
        if firstname.index(i) == 0:                     # we need only first element
            a = i.lower()                               # converting them to lower
    for j in lastname:                                  # looping char in lastname
        if lastname.index(j) == 0:                      # we need 3 elements of lastname
            a = a + j.upper()                           # first in upper form rest in lower case
        elif lastname.index(j) == 1:
            a = a + j.lower()
        elif lastname.index(j) == 2:
            a = a + j.lower()
    return a
print(create_id("John", "SMITH"))                       # Function calling and printing
