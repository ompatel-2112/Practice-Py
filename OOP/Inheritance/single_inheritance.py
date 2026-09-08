"""
Single inheritance enables a derived class to inherit properties from a single parent class,
thus enabling code reusability and the addition of new features to existing code
"""
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

obj = Child()
obj.func1()
obj.func2()

"""
Explanation:

The Child class inherits the method func1() from Parent.
It also has its own method func2().
This shows how one class can extend another using single inheritance.
"""