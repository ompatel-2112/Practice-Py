a = 3

b = 2

c = 16

print("bin>>>>", bin(a))

print("octal>>>>>", oct(a))

print("hexadecimal>>>>>", hex(c))

print("decimal>>>", int(0b10))

#Shifts the bits of a right by 3 positions
print(a >> 3)

#Shifts the bits of a left by 3 positions
print(a << 3)

#Bitwise AND - Compares bit by bit; result bit is 1 only if both bits are 1.
print(a & b)

#Bitwise OR -Result bit is 1 if either bit is 1.
print(a | b)

#Bitwise XOR - Result bit is 1 if the bits are different.
print(a ^ b)

#Bitwise NOT-Flips every bit
print(~a)