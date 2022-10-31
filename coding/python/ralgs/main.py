from algs import Algorithms
from colors import Colors



c = Colors()



def main():

    global OLL
    OLL = Algorithms().OLL()

    global PLL
    PLL = Algorithms().PLL()

    global c
    c = Colors()

    while True:
        cmd = input("\nCategory: ")
        if cmd == "1" or cmd.lower() == "oll":
            subtypes(OLL)

        if cmd == "2" or cmd.lower() == "pll":
            subtypes(PLL)

        if cmd.lower() == "ls" or cmd.lower() == "help":
            print("")
            for i in range(len(Algorithms().types)):
                print(str(i + 1) + ". " + Algorithms().types[i])



def subtypes(MainType):
    while 1:
        cmd = input("\nPattern: ")
        if cmd.lower() == "ls" or cmd.lower() == "help":
            print("")
            for i in range(len(MainType.types_readable)):
                print(str(i + 1) + ". " + MainType.types_readable[i])
        else:
            break
    for i in range(len(MainType.types_readable)):
        if cmd == str(i + 1) or cmd.lower() == MainType.types_readable[i].lower():
            printpatterns(getattr(MainType, MainType.types[i]))



def printpatterns(patternArray):
    for pattern, alg in zip(patternArray().patterns, patternArray().algs):
        print("\n" + formatpattern(pattern) + "\n" + alg)



def formatpattern(unformattedString):
    return unformattedString.replace("+", "  ").replace(">", "\n").replace("b", c.b + "▓▓").replace("B", c.b + "██").replace("g", c.g + "▓▓").replace("G", c.g + "██").replace("o", c.o + "▓▓").replace("O", c.o + "██").replace("r", c.r + "▓▓").replace("R", c.r + "██").replace("w", c.w + "▓▓").replace("W", c.w + "██").replace("y", c.y + "▓▓").replace("Y", c.y + "██").replace("n", c.w + "░░").replace("N", c.w + "▒▒") + c.reset



if __name__ == "__main__":
        main()
