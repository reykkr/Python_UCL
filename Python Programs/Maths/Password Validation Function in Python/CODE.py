password = input("Enter a password")
def valid(s):
    count_digts = 0
    count_cap = 0
    count_low = 0
    for c in s:
        if c >= 'A' and c <= 'Z':
            count_cap += 1
        elif c >= 'a' and c <= 'z':
            count_low += 1
        elif c >= '0' and c <= '9':
            count_digts +=1
        if len(s) < 8 or count_cap < 1 or count_low < 1 or count_digts < 2:
            return False
        else:
            return True
print(valid(password))