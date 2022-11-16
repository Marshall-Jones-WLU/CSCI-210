"""
Name: Marshall Jones
File: binary.py
Project1

Functions for decimal/binary conversions.
"""

def unsignedDecimalToBinary(n):
   '''Converts a decimal integer to a binary string'''
   # create an empty bit string
   bits = ""

   # if n is 0, set the bit string to "0"
   if n == 0:
      bits = "0"
   
   # while n is not 0, floor divide n by 2
   #and add the remainder to the bit string
   while n != 0:
      r = str(n%2)
      n //= 2
      bits = r + bits
   return bits

def unsignedBinaryToDecimal(bits):
   '''Converts a binary string to a decimal number'''
   # set number to 0
   number = 0

   # loop through the bit string from right-to-left
   #and multiply each bit by 2 to the power of the
   #index position in the bit string.
   for i in range(len(bits)):
      n = int(bits[-1-i])*(2**i)
      number += n
   return number

def addOne(unsignedBinary):
   '''Adds 1 to the bit string'''
   # turn the bit string to a list because
   #strings are immutable
   bits = list(unsignedBinary)

   # if the right-most bit is 0, just replace
   #it with 1
   if bits[-1] == '0':
      bits[-1] = '1'
   # otherwise, find the closest 0 to the right,
   #replace it with 1, and make the right-most
   #bit 0.
   else:
      for i in range(len(bits)):
         if bits[-1-i] == '0':
            bits[-1-i] = '1'
            bits[-1] = '0'
            break
   bits = ''.join(bits)
   return bits

def twosComplementToDecimal(twosComp):
   '''Converts a Two's Comp bit string to decimal'''
   if twosComp[0] == '1':
      # negate the bits, then the number
      return -1 * unsignedBinaryToDecimal(addOne(invert(twosComp)))
   else:
      return unsignedBinaryToDecimal(twosComp)

def decimalToTwosComplement(decimal):
   '''Converts a decimal number to a Two's Comp bit string'''
   if decimal < 0:
      # Negate the number, then the bits
      return "1" + addOne(invert(unsignedDecimalToBinary(-decimal)))
   
   else:
      return "0" + unsignedDecimalToBinary(decimal)

def signExtend(twosComp, n=8):
   '''Extends a Two's Comp bit string to a Byte'''
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

"""EXERCISE 2 FUNCTIONS"""
def unsignedFractionToBinary(unsignedFloat, nBits = 23):
   # create the fraction variable
   binaryFraction = ""

   # iterate through the number of bits we want in the string
   for i in range(nBits):

      # multiply the fraction by 2
      unsignedFloat *= 2
      # and add the whole number (1 or 0) to our fraction bit string variable
      binaryFraction += str(int(unsignedFloat))

      # if the product is greater than 1, subtract by 1
      if unsignedFloat >= 1:
         unsignedFloat -= 1
   
   return binaryFraction

def unsignedFloatToBinary(unsignedFloat, nBits = 31):
   # find the fractional part of the unsigned float by subtracting the integer
   #of unsignedFloat from unsignedFloat
   fraction = unsignedFloat - int(unsignedFloat)

   # return the binary string of the whole number, plus the binary string of the fractional part,
   #separated by a '.'
   return unsignedDecimalToBinary(int(unsignedFloat)) + '.' + unsignedFractionToBinary(fraction, nBits - 9)

def normalize(bitString):
   # find the index position of the decimal and assign to variable
   hops = bitString.index('.') - 1

   # split the string by the decimal and assign variables to each
   #end of the string
   left, right = bitString.split('.')

   return left[0] + '.' + left[1:] + right + 'E' + str(hops)

def decimalToSinglePrecision(signedFloat):
   # record the decimal's sign
   if signedFloat < 0:
      sign = '1'
   else:
      sign = '0'
   
   # find the mantissa. First convert absolute value of decimal to binary,
   #then normalize the bit string.
   mant = normalize(unsignedFloatToBinary(abs(signedFloat), 24))
   # find the biased exponent in binary string: add 127 to the exponent,
   #and get the bit string of that number.
   exp = unsignedDecimalToBinary(int(mant[-1]) + 127)
   # return the sign, exponent, and mantissa (without the first and last 2 digits)
   return sign + exp + mant[2:-2]

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
   print ("5 ->", twosComplementToDecimal("0101"))
##
   print ("-5 ->", twosComplementToDecimal("1011"))
##
   print ("0101 ->", decimalToTwosComplement(5))
##
   print ("1011 ->", decimalToTwosComplement(-5))
##
   print ("00000101 ->", signExtend(decimalToTwosComplement(5), 8))
##
   print ("11111011 ->", signExtend(decimalToTwosComplement(-5), 8))

def main2():
   """Test bed for float point to binary conversion functions"""
   print("unsignedFractionToBinary:")
   print("00111011 ->", unsignedFractionToBinary(.234, 8))

   print("")

if __name__ == "__main__":
   main()
   # main2()