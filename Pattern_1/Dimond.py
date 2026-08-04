Num=int(input("Enter a Number:"))

for i in range(Num):
    for j in range(Num-i):          # for space
        print(end=" ")
    for j in range(i+1):              # for inc Space and Decrease star
        print("*",end=" ")
    print()

for i in range(Num,-1,-1):
    for j in range(Num-i):          # for space
        print(end=" ")
    for j in range(i+1):              # for inc Space and Decrease star
        print("*",end=" ")
    print()