Num=int(input("Enter a Number to find Prime No:"))
New=0

for Prim in range(1,Num+1):
    count=0
    for i in range (1,Prim+1):
        if Prim%i==0:
            count=count+1
    if count==2:
        New=New+1

print("The numer of Prime Num between :%d"%New)

