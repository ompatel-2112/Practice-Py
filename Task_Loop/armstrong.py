#153
from linkify_it.ucre import TPL_HOST_FUZZY

Num=int(input("Enter the number : "))

x=len(str(Num))
one=0
two=0
three=0
four=0
Num1=0

if x == 4:
    Des= Num % 10

    Hun= Num // 10 % 10

    Thou= Num // 100 % 10

    Lac= Num // 1000 % 10

    one=Des
    two=Hun
    three=Thou
    four=Lac


if x == 3:
    Des=Num%10

    Hun=Num//10%10

    Thou=Num//100%10

    one = Des
    two = Hun
    three = Thou


if x == 4:
    one1 = one ** 4
    two1 = two ** 4
    three1 = three ** 4
    four1 = four ** 4

    Num1 = one1 + two1 + three1 + four1

elif x == 3:
    one1 = one ** 3
    two1 = two ** 3
    three1 = three ** 3

    Num1 = one1 + two1 + three1

if Num==Num1:
    print(Num1)
    print("Given number is armstrong")

else:
    print("Given number is not armstrong")





