Num=int(input("Enter no. students:"))
students={ }

for i in range(Num):
    X={ }

    X['rollno'] = input("Enter roll no:")
    X['name'] = input("Enter name:")
    X['marks'] = int(input("Enter marks:"))
    X['grade'] = None

    for j in X:
        Y="s"+str(i+1)
        students[Y] = X

        if students[Y]['marks'] >= 90 and students[Y]['marks'] <= 100:
            students[Y]['grade'] = 'A'
        elif students[Y]['marks'] >= 80 and students[Y]['marks'] < 90:
            students[Y]['grade'] = 'B'
        elif students[Y]['marks'] >= 60 and students[Y]['marks'] < 80:
            students[Y]['grade'] = 'C'
        elif students[Y]['marks'] >= 40 and students[Y]['marks'] <60:
            students[Y]['grade'] = 'D'
        else:
            students[Y]['grade'] = 'Fail'
print(students)

