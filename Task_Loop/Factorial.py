from streamlit.proto import NumberInput_pb2

Num=int(input("Enter a number:"))
Fact=1

if Num<=0:
    print("Factorial not Exist")
    exit()
else:
    for i in range(1,Num+1):
        Fact=Fact*i
print("Factorial of Given Num :%d"%Fact)