# declare the employee class
class Employee:
    """this is desc of employee class"""
    pass

def myfunction():
    """this is desc of my function"""
    print("this is my function")


# create object of the class.
emp_1 = Employee()
emp_2 = Employee()

# doc string
print(Employee.__doc__)

# this is desc of employee class

print(myfunction.__doc__)
# this is desc of my function


# print the result and you will find that each object is stored in different memory location.

print(emp_1)
# <__main__.Employee object at 0x00000294F1016B70>

print(emp_2)
# <__main__.Employee object at 0x00000294F1016EF0>

class Car:

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def display(self):
        print(self.name,self.brand)

    def car(self,color):
        print(self.name,self.brand,color)

c1=Car("thar","mahindra")
c1.display()
c1.car('black')