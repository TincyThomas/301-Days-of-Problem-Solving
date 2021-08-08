def is_valid(zip_code):
    count = 0
    a =[]
    if len(zip_code) == 5:
        for i in zip_code:
            try:
                if int(eval(i)) == int(i):
                    count = count+1
                    if count == len(zip_code):
                        return True
            except: return False


print(is_valid("12l01"))
