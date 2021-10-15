def is_palindrome(txt):
    text = ''.join(char for char in txt if char.isalnum())
    t = text[::-1]
    return True if text.lower() == t.lower() else False


print(is_palindrome("Not a palindrome"))
