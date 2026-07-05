import argparse
import sys

ERRMSG = "Error: wrong input!"

#Decimal to binary
def decToBin(number):
    try:
        return bin(int(number)).replace("0b", "")
    except ValueError:
        return ERRMSG

#Binary to Decimal
def binToDec(number):
    try:
        return str(int(number, 2))
    except ValueError:
        return ERRMSG
        
