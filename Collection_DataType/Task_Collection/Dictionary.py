Num=int(input("Enter no. students:"))

Student = { }

for i in range(1,Num+1):
    X="Roll No"+str(i)
    Y="Name"+str(i)
    Z="Marks"+str(i)
    Student[X] = int(input("Enter Student Roll No:"))
    Student[Y]= input("Enter Student Name:")
    Student[Z] = int(input("Enter Student Marks:"))
print(Student)

""" 
for i in range(Num):
    X="s"+str(Num)
    X={ }
    X['rollno'] = input("Enter roll no:")
    X['name'] = input("Enter name:")
    X['marks'] = input("Enter marks:")
    X['grade'] = None

print(X)

find the grade and assign

90 to 100->A grade assign

80 to 90->B grade assign

60 to 80->C grade assign

40 to 60->D grade assign

<40->Fail

"""