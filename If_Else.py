"""

1) user
input
a
character

a->"you have enter a"

b->"you have enter b"

c->"you have enter c"

->Invalid
character
 """
Enter_Char=input("Enter a character =")

if Enter_Char=="a":
    print("You have enter a")
elif Enter_Char=="b":
    print("You have enter b")
elif Enter_Char=="c":
    print("You have enter c")
else :
    print("invalid Character")

"""
2)user input a number

	positive number
		odd number
			perform addition with an integer constant

		even number
			perform multiplication with an floating point constant

	negative number
		odd number
			perform subtraction with an integer constant

		even number
			perform division with an floating point constant
"""
Num=int(input("Enter a number="))

X=10
Y=20

if Num>0:
    if Num%2!=0:
        print("Odd number")
        print("%d"%(X+Num))
    else:
        print("even number")
        print("%f"%(Y*Num))
elif Num<0:
    if Num % 2 != 0:
        print("Odd number")
        print("%d"%(Num-X))
    else:
        print("even number")
        print("%f"%(Y/Num))
else:
    print("You Enterd Zero!")

"""
3)user input marks

	90 to 100->A grade
	
	80 to 90->B grade
	
	60 to 80->C grade
	
	40 to 60->D grade
	
	< 40     ->Fail
	
	>100 	->Invalid Marks  """

Entr=int(input("Enter Your marks ="))

if Entr>=90 and Entr<=100:
    print("A grade")
elif Entr>=80 and Entr<=90:
    print("B grade")
elif Entr>=60 and Entr<=80:
    print("C grade")
elif Entr>=40 and Entr<=60:
    print("D grade")
elif Entr>100:
    print("Invalid Marks")
else:
    print("Fail in  Exam")

