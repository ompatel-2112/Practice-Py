# Dictionary functions

"""
{} -json format
it will consider dictionary format
in key pair value                        """

# general function
dict = {'Name': 'Abc', 'Age': 18}
print(dict)
print(len(dict))

asit = {'Name': 'Abc', 'Age': 18}
print(type(asit))

a = str(dict)
print(a[2])
print(type(a))

# function of dictionary
dict.clear()  #clear the dictionary
print(dict)
print(len(dict))

# copy whole dictionar
dict1 = {'Name': 'Abc', 'Age': 7}
abc = dict1.copy()
print("Copy Data",abc)

# the formkeys it convert data from tupl to dictionary
tupl = ('name','abc')
the = dict.fromkeys(tupl) ## in above its only key so it will return none value
print(the)

# if we pass its value it will consider in all keys as same value
dict = dict.fromkeys(tupl, 10)
print(dict)

# base on key we get the value using finctoin of get
dict = {'Name': 'abc', 'Age': 7}
print(dict.get('Age'))
# if we pass the key which are not exist the it return never
print(dict.get('Education', "Never"))


#  in the items functoin base on key we get the value in tuple in list
dict = {'Name': 'Abc', 'Age': 7}
print(dict.items())

# in this we get the value of keys
print(dict.values())

# in this we get the keys
print(dict.keys())

# for update dictionary
dict1 = {'Name': 'xyz', 'Age': 7}
dict2 = {'Gender': 'male'}
dict1.update(dict2)
print(dict1)
print(dict2)