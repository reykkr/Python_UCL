s = eval(input("enter a word: "))
a = eval(input("enter first letter: "))
b = eval(input("enter second letter: "))
def replace(s,a,b):
    edit = ''
    for i in s:
        if i == a:
            edit = edit + b
        else:
            edit = edit + i
    return edit
print(replace(s,a,b))