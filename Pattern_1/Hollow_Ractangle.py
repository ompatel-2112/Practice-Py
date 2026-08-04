Num=int(input("Enter Num:"))


for i in range(Num):
    for j in range(Num):
        if i==0 or j==0 or i==Num-1 or j==Num-1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

