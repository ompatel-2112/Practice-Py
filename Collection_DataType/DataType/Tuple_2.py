
""" Tuple : Tuples are ordered immutable sequence that stores multiple items in a single variable, meaning it cannot
 be changed after it has been created. A tuple can be created by a pair of parenthesis and comma-separated
 objects, following the variable name. """

S = (1,1,'a',10.8,'abc')

print(S)

print(type(S))

print("Length of List :",len(S))

print(S[0])

print(S[2:4])

print(S[3:])

print(S[4::-1])

print(S[1])

print(S)

print(S[:3])

# S[3]=10 can't change or Update the value of any Index

print(S)
