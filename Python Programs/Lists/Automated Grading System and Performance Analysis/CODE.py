answers = [['A','C','D','A','A'],['B','B','C','C','C'],['A','D','A','A','E']]
key = ['A','C','A','E','A']
grades = []
for std in range(len(answers)):
    count = 0
    grade = 0
    for letter in range(len(answers[std])):
        if answers[std][letter] == key[letter]:
            count += 1
    grades.append(count * 20)
print(grades)
average = 0
for i in grades:
    average += i
print("average is", average/std)
def insert(list):
        for i in range(1, len(list)):
            key = list[i]
            j = i - 1
            while j >= 0 and key <= list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = key
        return list
insert(grades)
print("min is", grades[0])
print("max is", grades[-1])