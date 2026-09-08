"""
Multiple Inheritance
When a class can be derived from more than one base class this type of inheritance is called
multiple inheritances. In multiple inheritances, all the features of the base classes are
inherited into the derived class
"""
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

"""
Explanation:

Son inherits from both Mother and Father.
It can access both mothername and fathername.
This demonstrates how a class can combine functionalities from multiple sources.
"""