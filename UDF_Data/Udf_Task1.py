"""
user will input the string

1) word wise reverse

2) two characters interchange """


x=str(input("Enter your string:"))

def Wwr(s):
    T=s.split(" ")
    for i in range(len(T)):
        print(T[i][::-1],end=" ")
    print()

Wwr(x)

def tci(w):
    T=w.split(" ")
    for i in range(len(T)):
        for j in range(0,len(T[i]),2):
            print(T[i][j:2+j][::-1], end="")

        print(end=" ")


tci(x)
