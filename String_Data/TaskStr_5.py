s="this is string example"

""" 
print(len(s))

print(s[::-1]) 
"""

#2) word wise reverse

T=s.split(" ")
print(T)

print(T[0][::-1],T[1][::-1],T[2][::-1],T[3][::-1])


#3) 2 characters interchange


print(T[0][0:2][::-1]+T[0][2:4][::-1],
      T[1][0:2][::-1],T[2][0:2][::-1]+T[2][2:4][::-1]+T[2][4:6][::-1],T[3][0:2][::-1]+T[3][2:4][::-1]+T[3][4:6][::-1]+T[3][6:][::-1])


#4)	space split join the string with *

New=s.split(" ")

Joined="*".join(New)

print(Joined)

#5) replace is -> was , substring-> this this is  was

print(s.replace(" is"," was"))

