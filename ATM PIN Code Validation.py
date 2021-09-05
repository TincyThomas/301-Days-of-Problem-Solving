def is_valid_PIN(pin):
    if type(pin) != str:
        a = str(pin)
        if len(a) == 4 or len(a) == 6:
            return True
        else: return False
    else:
        return False
print(is_valid_PIN(1234))
