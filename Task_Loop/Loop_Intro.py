# Foor Loop -> when we konw how many times Loop execute and must have Terminated condition

"""
for i in range(0,10,1):
               ^ ^ ^
            start end step

when we use Integer then use Range keyword

when we use String than use in keyword
"""
s = "hello"
for i in s:
    print(i)

for i in range(10):
    Len=i
    print(Len)

for i in range(0,10,2):
    print(i,end=" ")

for i in range(0,10):
    if i%2==0:
        print(i)

#Break-Stop Loop

for i in range(1,10):
    print(i)
    if i==5:
        break
else:
    print("End of loop")