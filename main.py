import argparse
import numberconv
import menu

def main():
    parser = argparse.ArgumentParser(description="Simple Number-Converter.")
    parser.add_argument("--deztobin", metavar="<NUMBER>", help="Convert immediately, Decimal to Binary", type=str)
    args = parser.parse_args()

    #Convert immediately
    if args.deztobin:
        ergebnis = numberconv.dezToBin(args.deztobin)
        print(f"{ergebnis}")
        
    #Open menu
    else:
        menu.showMenu()

if __name__ == "__main__":
    main()