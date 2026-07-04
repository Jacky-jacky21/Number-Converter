import argparse
import sys

def dezToBin(number):
    try:
        return bin(int(number)).replace("0b", "")
    except ValueError:
        return "Error: wrong input!"

