a = 20
b = 30

# return True if same
if a is b:

    print("answer 1 -same ")

else:

    print("answer 1 - not same")

# return true if same
if id(a) == id(b):

    print("answer 2 - same")

else:

    print("answer 2 - not same")


b = 30

if a is b:

    print("answer 3 - same")

else:

    print("answer 3 - not same")

if a is not b:

    print("answer 4 - not same")
else:

    print("answer 4 - same")
# print stored location of var
print(id(a))
print(id(b))