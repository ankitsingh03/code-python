def is_palindrom(name):
    reverse = name[ : :-1]
    if name == reverse:
        return True
    return False

print(is_palindrom("naman"))


# shot code
# def is_palindrom(name):
#     return name == name[ : :-1]
# print(is_palindrom("madam"))