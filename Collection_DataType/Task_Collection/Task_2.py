"""

user input values in a variable like

a=1,a,2,b,3,4,55,asit,nimesh

str_list=[]

int_list=[]

store int values inside int_list as integer
    -perform min and max function

store string values inside str_list as string
    -perform reverse function

"""
Inpt=input("Enter a List Element: ")
List=Inpt.split(",")
str_list=[]
int_list=[]

for x in List:
    if x.isdigit():
        int_list.append(int(x))
    elif x.isalpha():
        str_list.append(x)
print("Str List",str_list)
print("Int List :",int_list)
print("Max in list",max(int_list))
print("Min in list",min(int_list))
(str_list).reverse()
print(str_list)