students = int(input("Enter number of students"))
list = []
total_sum = 0
count = 0
for i in range(students):
    list.append(eval(input("Enter grade for student ")))
    total_sum += list[i]
average = total_sum / students
print(average)
for i in range(students):
    if list[i] > average:
        count += 1
print(count, "students passed")