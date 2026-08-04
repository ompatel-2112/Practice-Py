Num=int(input("Enter a number: "))
P=0
K=1
for i in range(Num):

    for j in range(Num-i):          # for space
        print(end=" ")
    for j in range(i+1):

        if 0==i%3:
            P="@"
        elif 1==i%3:
            P="$"
        elif 2==i%3:
            P=K
            K+=1

        print(P,end=" ")
    print()