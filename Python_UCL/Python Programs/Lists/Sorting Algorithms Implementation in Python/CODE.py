# Selection sorted list

def selection(lst):
    for i in range(len(lst) - 1):
        min = i
        for j in range(i + 1 , len(lst)):
            if lst[j] < lst[i]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("elements: "))
    list.append(ele)
print("sorted selection: ", selection(list))

# Insertion sorted list

def insert(list):
        for i in range(1, len(list)):
            key = list[i]
            j = i - 1
            while j >= 0 and key <= list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = key
        return list
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("elements: "))
    lst.append(ele)
print("sorted selection: ", insert(lst))