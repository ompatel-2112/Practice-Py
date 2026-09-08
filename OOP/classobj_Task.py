# from Import_statement.Task_1 import fn4

class StudentInfo:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

class StudentMarks:
    def __init__(self,marks_one,marks_two,marks_three):
        self.marks_one = marks_one
        self.marks_two = marks_two
        self.marks_three = marks_three

    def average(self):

        avg = (self.marks_one + self.marks_two + self.marks_three)//3
        return avg

class MainClass:
    def __init__(self,num):
        self.num = num
        avg_list = []
        for i in range (self.num):
            s1=StudentInfo(i,i)
            s1.rollno = int(input("Enter roll no:"))
            s1.name = input("Enter name:")
            s2=StudentMarks(i,i,i)
            s2.marks_one=int(input("Enter marks 1:"))
            s2.marks_two=int(input("Enter marks 2:"))
            s2.marks_three=int(input("Enter marks 3:"))
            avg_list.append(s2.average())
        print(avg_list)

m1=MainClass(int(input("Enter No of Students:")))







