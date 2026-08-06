# Function of  list

# General Function of list

# Length Function

list1, list2 = [123, 'xyz', 'Nimesh'], [456, 'abc']
print(len(list1))
print(len(list2))

# convert tuple value in list

aTuple = (123, 'xyz', 'Nimesh', 'abc')
aList = list(aTuple)
print(aTuple)
print("List elements :", aList)

# min,max Function
list3 = [123, 45 , 3 , 2 ]
print(max(list3))
print(min(list3))

#Function of list

# 1.append-append is used to update the data
aList= [123, 'xyz', 'Nimesh', 'abc']
aList.append(2009)
print("Updated List : ", aList)

# 2.count-to count how many types the number repeat

aList1 = [123, 'xyz', 'Nimesh', 'abc', 123]

print("Count for 123 : ", aList1.count(123))

# 3.Extend-if we want to update the list we use this function

aList = [123, 'xyz', 'Harshal', 'abc', 123]
bList = [2009, 'Nimesh',123]
aList.extend(bList)
print("Extended List : ", aList)

# 4. index
# it wll find the position

aList = [123, 'xyz', 'Nimesh', 'abc']
print("Index for Nimesh : ", aList.index('Nimesh'))

# 5.insert
# this function help to insert data at which position that will given

aList = [123, 'xyz', 'Nimesh', 'abc']
aList.insert(3, 2009)
# position index and data that we have to insert at the particular index
print("Final List : ", aList)

# 6.pop
# it will remove fom last

aList = [123, 'xyz', 'Nimesh', 'abc']
print("A List : ", aList.pop())
print(aList)

print("B List : ", aList.pop(2)) # if we want to remove from index we have to pass the argument like this
print(aList)


# 7.remove

aList = [123, 'xyz', 'Nimesh', 'abc', 'xyz']
aList.remove('xyz') # using this function remove from the list
print("List : ", aList)


# 8. reverse - using this function it reverse the string

aList = [123, 'xyz', 'Nimesh', 'abc', 'xyz']
aList.reverse()
print("List : ", aList)

#9. sort- it will sort list in assending order
aList = [47.5, 123, 123456789.66666666,5]
aList.sort()
print("List : ", aList)
