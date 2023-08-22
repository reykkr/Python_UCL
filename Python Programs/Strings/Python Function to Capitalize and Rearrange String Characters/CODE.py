string = input("Enter a string: ")
def capital(s):
    cap = ""
    small = ""
    for i in s:
        if 'A' <= i <= 'Z':
            cap = cap + i
        else:
            small = small + i
    complete = cap + small
    return complete
print(capital(string))