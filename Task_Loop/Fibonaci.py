Num=int(input("Enter a number: "))

a=0
b=1
c=0
print(a)
print(b)

for i in range(0,Num):
    c=a+b
    print(c)
    a=b
    b=c
    if c >= Num:
        break
