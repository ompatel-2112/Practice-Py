"""
Hybrid Inheritance
Hybrid inheritance is a combination of more than one type of inheritance.
It uses a mix like single, multiple, or multilevel inheritance within the same program
"""
class School:
    def func1(self):
        print("This function is in school.")

class Student1(School):
    def func2(self):
        print("This function is in student 1.")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

obj = Student3()
obj.func1()
obj.func2()

"""
Explanation:
School is the base class inherited by Student1, Student2, and Student3.
Student1 and Student2 each inherit School (single inheritance).
Student3 inherits both from Student1 and School (multiple inheritance).
Python handles method resolution using the MRO, so func1() from School is resolved without ambiguity.
"""