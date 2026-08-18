
f1=open("Task1.txt","w+")
Num=int(input("enter no of lines:"))
def file_inp(lines):
    for i in range(lines):
        f1.write(input("enter Data for line"+"%d"%(i+1)+":"))
        f1.write(" \n")
    file_task()

# count lines,words,with space chars & without space chars

def file_task():
    f1.seek(0)
    data=f1.read()
    print(data)

    lst1=data.split("\n")
    count1=0
    for i in lst1:
        count1=count1+1
    print("number of lines : ",count1-1)

    lst1 = data.split(" ")
    count2 = 0
    for i in lst1:
        count2 = count2 +1
    print("number of words : ", count2-1 )

    Len1=len(data)
    print("With space Characters : ",Len1-(count1-1))
    print("Without Space Characters : ",Len1-(count1+count2-2))


file_inp(Num)



f1.close()