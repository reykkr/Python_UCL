answers = [['A','C','D','A','A'],['B','B','C','C','C'],['A','D','A','A','E']]
key = ['A','C','A','E','A']
for std in range(len(answers)):
    count = 0
    for letter in range(len(answers[std])):
        if answers[std][letter] == key[letter]:
            count += 1
    print("Student score is ", count)