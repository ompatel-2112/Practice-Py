Num = int(input("Enter a number: "))
k=1
for i in range(Num):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()
