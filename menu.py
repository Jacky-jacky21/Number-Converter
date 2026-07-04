import sys 
import numberconv

def showMenu():
    print("=== Welcome to the converter menu! ===")
    print("1) Dezimal to Binary")
    print("2) exit \n")

    selection = input("Please choose an option(1-2): ")

    if selection == "1":
        number = input("Please enter the decimal number: ")
        print(numberconv.dezToBin(number))
    elif selection == "2": 
        print("Converter closed")
        sys.exit()
    else:
        print("Invalid selection.")