"""
Name: Marshall Jones
File: binary.py
Project1

Functions for decimal/binary conversions.
"""

'''
EXERCISES 1-4
1. Interpret the eight bit string 01101100 as
   a. a two's complement eight bit number
      10010110
   b. a sign-magnitude eight bit number
      01101100
   c. an unsigned binary number
      01101100

2. Interpret the eight bit string 11001101 as
   a. a two's complement eight bit number
      00110011
   b. a sign-magnitude eight bit number
      11001101
   c. an unsigned binary number
      11001101

3. Represent the following integer values as eight 
   bit two's complement numbers:
   a. 56
      00111000
   b. -43
      11010101
   c. -1
      11111111

4. Convert the following values to hexadecimal notation
   a. 56 (decimal)
      –> 38
   b. 438 (decimal)
      –> 1B6
   c. 11010111 (binary)
      –> D7
'''

def unsignedDecimalToBinary(n):
   bits = []
   if n == 0:
      bits.insert(0,'0')
   while n != 0:
      r = str(n%2)
      n = n//2
      bits.insert(0, r)
   bits = ''.join(bits)
   return bits

def unsignedBinaryToDecimal(unsignedBinary):
   bits = list(unsignedBinary)
   number = 0
   for i in range(len(bits)):
      n = int(bits[-1-i])*(2**i)
      number += n
   return number

def addOne(unsignedBinary):
   bits = list(unsignedBinary)
   if bits[-1] == '0':
      bits[-1] = '1'
   else:
      for i in range(len(bits)):
         if bits[-1-i] == '0':
            bits[-1-i] = '1'
            bits[-1] = '0'
   bits = ''.join(bits)
   return bits

def twosCompToDecimal(twosComp):
   if twosComp[0] == '1':
      # negate the bits, then the number
      return -1 * unsignedBinaryToDecimal(addOne(invert(twosComp)))
   else:
      return unsignedBinaryToDecimal(twosComp)

def decimalToTwosComp(decimal):
   if decimal < 0:
      # Negate the number, then the bits
      return "1" + addOne(invert(unsignedDecimalToBinary(-decimal)))
   
   else:
      return "0" + unsignedDecimalToBinary(decimal)

def signExtend(twosComp, n=8):
   left = twosComp[0]

   while len(twosComp) < n:
      twosComp = left + twosComp
   return twosComp

def invert(bitString):
   """Returns the bit string with the bits inverted."""
   invertedString = ''
   for bit in bitString:
      if bit == '1':
         invertedString += '0'
      else:
         invertedString += '1'
   return invertedString

def main():
   """Test bed for decimal/binary conversion functions."""
   print ("11001 ->", invert("00110"))

   print ("0 ->", unsignedBinaryToDecimal("0"))
##
   print ("6 ->", unsignedBinaryToDecimal("110"))
##
   print ("0 ->", unsignedDecimalToBinary(0))
##
   print ("110 ->", unsignedDecimalToBinary(6))
##
   print ("110 ->", addOne("101"))
##
   print ("5 ->", twosCompToDecimal("0101"))
##
   print ("-5 ->", twosCompToDecimal("1011"))
##
   print ("0101 ->", decimalToTwosComp(5))
##
   print ("1011 ->", decimalToTwosComp(-5))
##
   print ("00000101 ->", signExtend(decimalToTwosComp(5), 8))
##
   print ("11111011 ->", signExtend(decimalToTwosComp(-5), 8))

if __name__ == "__main__":
   main()
