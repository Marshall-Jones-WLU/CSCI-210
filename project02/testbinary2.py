"""
File: testbinary2.py
Tester program for IEEE floating-point conversions.
"""

from binary import *

print("Convert .65625 to unsigned fraction, 10101 ->", unsignedFractionToBinary(.65625, 25))

print("Convert .45 to unsigned fraction, 0111001100110011001100110 ->", unsignedFractionToBinary(.45, 25))

print("Convert 312.875 to unsigned float, 100111000.111 ->", unsignedFloatToBinary(312.875, 25))

print("Convert 312.875 to normalized unsigned float, 1.00111000111E8 ->", normalize(unsignedFloatToBinary(312.875, 25)))

print("Convert 312.875 to IEEE float, 01000011100111000111000000000000 ->", decimalToSinglePrecision(312.875))
