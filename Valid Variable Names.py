def variable_valid(var):
    if " " not in var:                  # we do not want space in between
        a = var[0]                      # taking first element
        if a.isalpha():                 # checking first element to be an alphabet
            return True                 # True if both condition matches
    else:
        return False                    # otherwise false
print(variable_valid("TimesN"))
