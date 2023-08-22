# user inputs a list, it should be written in this format: [[4,5],[8,7],[9,3]]

user_input = input("Enter a 2D list: ")

list = eval(user_input)

# or use a generated list

list = [[4,5],[8,7],[9,3]]

def m(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j > 1:
                print("List should only have 2 columns")
                return ""
    for row in lst:
        row[0],row[1] = row[1],row[0]
    for i in lst:
        print(i)
    return  ""
print(m(list))