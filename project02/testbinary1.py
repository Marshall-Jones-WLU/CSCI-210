"""
File: testbinary1.py
Tester program for unsigned integer conversions.
"""

from binary import *

print ("0 ->", unsignedBinaryToDecimal("0"))

print ("6 ->", unsignedBinaryToDecimal("110"))

print ("0 ->", unsignedDecimalToBinary(0))

print ("110 ->", unsignedDecimalToBinary(6))

print ("11001 ->", invert("00110"))

print ("110 ->", addOne("101"))

print ("5 ->", twosComplementToDecimal("0101"))

print ("-5 ->", twosComplementToDecimal("1011"))

print ("0101 ->", decimalToTwosComplement(5))

print ("1011 ->", decimalToTwosComplement(-5))

print ("00000101 ->", signExtend(decimalToTwosComplement(5), 8))

print ("11111011 ->", signExtend(decimalToTwosComplement(-5), 8))

print("The first 8 non-negative signed integers, sign-extended to 4 bits:")
for decimal in range(8):
    print(decimal, signExtend(decimalToTwosComplement(decimal), 4))
      
print("The first 8 negative signed integers, sign-extended to 5 bits:")
for decimal in range(1, 9):
    print(-decimal, signExtend(decimalToTwosComplement(-decimal), 5))

print("The first 8 negative signed integers and their absolute values:")
for decimal in range(1, 9):
    print(-decimal, signExtend(decimalToTwosComplement(-decimal), 5),
          addOne(invert(decimalToTwosComplement(-decimal))))
