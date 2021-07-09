def same_case(txt):
    if txt.isupper() or txt.islower():                # checking lower case and uppercase
        return "True"
    else:
        return "False"                                # False when it is in mixed case

print(same_case("hellO"))
