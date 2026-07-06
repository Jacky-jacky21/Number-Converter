import argparse
import numberconv
import menu

def main():
    parser = argparse.ArgumentParser(description="Simple Number-System-Converter.")
    parser.add_argument("-db", "--dectobin", metavar="<DEC>", help="Convert Decimal to Binary", type=str)
    parser.add_argument("-dh", "--dectohex", metavar="<DEC>", help="Convert Decimal to Hexadecimal", type=str)
    parser.add_argument("-bd", "--bintodec", metavar="<BIN>", help="Convert Binary to Decimal", type=str)
    parser.add_argument("-bh", "--bintohex", metavar="<BIN>", help="Convert Binary to Hexadecimal", type=str)
    parser.add_argument("-hd", "--hextodec", metavar="<HEX>", help="Convert Hexadecimal to Decimal", type=str)
    parser.add_argument("-hb", "--hextobin", metavar="<HEX>", help="Convert Hexadecimal to Binary", type=str)
    args = parser.parse_args()

    #Convert immediately
    #dtb
    if args.dectobin:
        result = numberconv.decToBin(args.dectobin)
        print(result)

    #dth
    #TODO: Test it
    elif args.dectohex:
        result = numberconv.decToHex(args.dectohex)
        print(result)
        
    #btd
    elif args.bintodec:
        result = numberconv.binToDec(args.bintodec)
        print(result)

    #bth
    #TODO: Test it
    elif args.bintohex:
        result = numberconv.binToHex(args.bintohex)
        print(result)

    #htd
    #TODO: Test it
    elif args.hextodec:
        result = numberconv.hexToDec(args.hextodec)
        print(result)

    #htb
    #TODO: Test it
    elif args.hextobin:
        result = numberconv.hexToBin(args.hextobin)
        print(result)

    #Open menu
    else:
        print("=== Welcome to the converter menu! ===")
        while True:
            menu.showMenu()

if __name__ == "__main__":
    main()