"""
What is UDF : Function which is Defined or create by the User And it can be Use for multiple time
-> we use def keyword for define the function
"""

def f():
    print("Hello")
f()

#we can pass argument in udf

# function fn1() call
def f1(a):
    print(a)
f1("argument pass")

# pass 2 and return 2

def fun(a,b):
    print(a)
    print(b)

fun("argument pass 1","argument pass 2")

"""

#passing one argument

def f2(a,b):
    print(a)
    print(b)

f2("New day") # throw error

#passing double argument and return one

def f3(c):
    print(c)

f("hello","yellow") # throw 

"""

def f4(a,b):
    print(a+b)
    print(a-b)

f4(20,10)

# return argument and store in var

def f5(a,b):
    c=a+b
    d=a-b
    return c,d

x,y=f5(40,20)
print(x,y)

# 1. function without arguement with return "none
def fn1():
    print("This is User Define function !")
    # none
    return

#Recursion - Function call it self and must have termination condition(decries order)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

Result=fact(int(input("enter num to find factorial:")))
print(Result)

