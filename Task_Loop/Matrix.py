Num1=int(input("Enter a Row:"))
Num2=int(input("Enter a Column:"))

for i in range(0,Num1):
    print("|",end="")
    for j in range(0,Num2):
        print(" %d"%(i),end="")
        print("%d"%(j),end="")
    print(" |", end="")
    print()
