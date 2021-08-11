def is_palindrome(n):
    a = ""
    for i in str(n):
        a = i + a
    return True if a == str(n) else False
print(is_palindrome(738))
