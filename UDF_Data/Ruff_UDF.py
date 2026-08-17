def calculate(*lst):
    for element in lst:
        List1=element

    if len(List1)==1:
        print(List1)
    elif len(List1)==2:
        List1[0].extend(List1[1])
        print(List1[0])
        print(max(List1[0]))
        print(min(List1[0]))
    elif len(List1)==3:
        List1[0].extend(List1[1])
        List1[0].extend(List1[2])
        print(List1[0])
        SUM=0
        for k in List1[0]:
            SUM+=k
        print("Internal Addition of All Elements :",SUM)
    elif len(List1)>4:
        for l in range(len(List1)-1):
            List1[0].extend(List1[l+1])
        lst_new=list(map(lambda x:x * x,List1[0]))
        print(lst_new)
        Odd_List=list(filter(lambda x: (x % 2 != 0),List1[0]))
        print(Odd_List)
    else:
        print("Invalid Input")

No_List=int(input("Enter the no. of list:"))
List=[]
if No_List==1:
    List1=[]
    X = int(input("Enter the No of Element for list :"))
    for i in range(X):
        List1.append(int(input("Enter the No of Element for list :")))
    calculate(List)
elif No_List==2:
    List1=[]
    List2=[]
    X = int(input("Enter the No of Element for list 1 :"))
    for i in range(X):
        List1.append(int(input("Enter the Element for list 1:")))
    Y = int(input("Enter the No of Element for list 2:"))
    for j in range(Y):
        List2.append(int(input("Enter the Element for list 2:")))
    calculate(List1,List2)
elif No_List==3:
    List1 = []
    List2 = []
    List3 = []
    X = int(input("Enter the No of Element for list 1 :"))
    for i in range(X):
        List1.append(int(input("Enter the Element for list 1:")))
    Y = int(input("Enter the No of Element for list 2:"))
    for j in range(Y):
        List2.append(int(input("Enter the Element for list 2:")))
    z = int(input("Enter the No of Element for list 3:"))
    for k in range(Y):
        List3.append(int(input("Enter the Element for list 3:")))
    calculate(List1,List2,List3)
