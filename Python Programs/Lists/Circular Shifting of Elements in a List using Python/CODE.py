list = [10,20,30,40]
def shift(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        lst[i-1] = lst[i]
    lst[len(lst) - 1] = a
    return lst
print(shift(list))

# another way

# def shift(lst):
#     shifted = []
#     for i in range(1, len(lst)):
#         shifted.append(lst[i])
#     shifted.append(lst[0])
#     return shifted
# print(shift(list))