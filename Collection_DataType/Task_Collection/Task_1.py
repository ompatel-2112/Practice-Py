ls= [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6, ['d', 'e', 'f'], 7, 'g', 8, 'h', ['9', '10', 'i', 'j'],11,'aansh']

for x in ls:
    if type(x)==int:
        print(x)
    elif type(x)==str:
        for y in x:
            print("            ",y)
    elif type(x)==list:
        for i in x:
            if i.isdigit():
                print(i)
            elif i.isalpha():
                print("            ",i)
    else:
        print("invalid")
