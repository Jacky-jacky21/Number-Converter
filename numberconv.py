import argparse
import sys

#For fast convertion without opening menu
def dezToBin(number):
    try:
        return bin(int(number)).replace("0b", "")
    except ValueError:
        return "Error: wrong input!"



#With menu 
#coming soon...