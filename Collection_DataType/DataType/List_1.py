"""
1.List : Lists are ordered mutable sequences that can be changed after they have been created by
 adding, removing, or changing objects.
 Lists can be declared by using square brackets “[]” following the variable name."""

S = [1,1,'a',10.8,'abc']

print(S)

print(type(S))

print("Length of List :",len(S))

print(S[0])

print(S[2:4])

print(S[3:])

print(S[4::-1])

S[1]=False

print(S[1])

print(S)

print(S[:3])

name = [[1, 2, 3, 4, 5, 6], ["Dhairya", "Rahul", "ASit"]]

print(name)

print(type(name))

print(name[0][0]) # print from 1st list of index 0 = 1

print(name[1][1]) # print from 2nd list of index 1 = Rahul