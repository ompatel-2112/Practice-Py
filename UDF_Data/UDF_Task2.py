# user will decide no. of lists
# 2
#
# user wil input no. of elements for each list
# ls1=>5
# ls2=>7
#
# user will input element for each list
# ls1=[1,11,43,56,43]
# ls2=[1,32,3,4,5,6,7]
# calculate(ls1)=>print the list
#
# calculate(ls1,ls2)=>
# concate both the lists=>
# print maximum-minimum element
#     56,1
#
# calculate(ls1,ls2,ls3)=>
# concate all the lists=>
# print internal addition of all elements
#
#
# calculate(n list)=>concate all the lists
# lambda function
#     print the square of every element and store in list
#     find the odd number and store in list

def calculate(*lst):

    List1 = list(lst)

    if len(List1) == 1:
        print(List1[0])
    elif len(List1) == 2:
        List1[0].extend(List1[1])
        print(List1[0])
        print(max(List1[0]))
        print(min(List1[0]))
    elif len(List1) == 3:
        List1[0].extend(List1[1])
        List1[0].extend(List1[2])
        print(List1[0])
        SUM = 0
        for k in List1[0]:
            SUM += k
        print("Internal Addition of All Elements :", SUM)

    else:
        for l in range(len(List1)-1):
            List1[0].extend(List1[l+1])
        lst_new=list(map(lambda x:x * x,List1[0]))
        print(lst_new)
        Odd_List=list(filter(lambda x: (x % 2 != 0),List1[0]))
        print(Odd_List)


No_List = int(input("Enter the no. of list: "))

if No_List == 1:
    List1 = []
    X = int(input("Enter the No of Element for list: "))
    for i in range(X):
        List1.append(int(input("Enter the Element for list: ")))
    calculate(List1)

elif No_List == 2:
    List1 = []
    List2 = []
    X = int(input("Enter the No of Element for list 1 : "))
    for i in range(X):
        List1.append(int(input("Enter the Element for list 1: ")))
    Y = int(input("Enter the No of Element for list 2: "))
    for j in range(Y):
        List2.append(int(input("Enter the Element for list 2: ")))
    calculate(List1, List2)

elif No_List == 3:
    List1 = []
    List2 = []
    List3 = []
    X = int(input("Enter the No of Element for list 1 : "))
    for i in range(X):
        List1.append(int(input("Enter the Element for list 1: ")))
    Y = int(input("Enter the No of Element for list 2: "))
    for j in range(Y):
        List2.append(int(input("Enter the Element for list 2: ")))
    z = int(input("Enter the No of Element for list 3: "))
    for k in range(z):
        List3.append(int(input("Enter the Element for list 3: ")))
    calculate(List1, List2, List3)

else:
    List=[]
    for i in range(No_List):
        List_New = []
        X = int(input("Enter the No of Element for list"+ "%d"%(i+1)+" :"))
        for j in range(X):
            List_New.append(int(input("Enter the element for list :")))
        List.append(List_New)
    calculate(*List)
