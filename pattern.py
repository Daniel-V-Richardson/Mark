height = 5

width = (2 * height) - 1


def printA():

    n = width // 2
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n-1


def printB():
    half = height // 2

    for i in range(0, height):
        print("*", end="")
        for j in range(0, width):
            if ((i == 0 or i == height - 1 or i == half) and j < (width - 2)):
                print("*", end="")
            elif (j == (width - 2) and not (i == 0 or i == height - 1 or i == half)):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printC():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height - 1):
            if (i == 0 or i == height - 1):
                print("*", end="")
            else:
                continue
        print()


def printD():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height - 1) and j < height - 1):
                print("*", end="")
            elif (j == height - 1 and i != 0 and i != height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printE():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height - 1) or (i == height // 2 and j <= height // 2)):
                print("*", end="")
            else:
                continue
        print()


def printF():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0) or (i == height // 2 and j <= height // 2)):
                print("*", end="")
            else:
                continue
        print()


def printG():

    for i in range(0, height):
        for j in range(0, width-1):
            if ((i == 0 or i == height - 1) and (j == 0 or j == width - 2)):
                print(end=" ")
            elif (j == 0):
                print("*", end="")
            elif (i == 0 and j <= height):
                print("*", end="")
            elif (i == height // 2 and j > height // 2):
                print("*", end="")
            elif (i > height // 2 and j == width - 2):
                print("*", end="")
            elif (i == height - 1 and j < width - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printH():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((j == height - 1) or (i == height // 2)):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printI():

    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printJ():

    for i in range(0, height):
        for j in range(0, height):
            if (i == height - 1 and (j > 0 and j < height - 1)):
                print("*", end="")
            elif ((j == height - 1 and i != height - 1) or (i > (height // 2) - 1 and j == 0 and i != height - 1)):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printK():
    half = height // 2
    dummy = half
    for i in range(0, height):
        print("*", end="")
        for j in range(0, half+1):
            if (j == abs(dummy)):
                print("*", end="")
            else:
                print(end=" ")
        print()
        dummy = dummy - 1


def printL():

    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (i == height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printM():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (j == height):
                print("*", end="")
            elif (j == counter or j == height - counter - 1):
                print("*", end="")
            else:
                print(end=" ")
        if (counter == height // 2):
            counter = -99999
        else:
            counter = counter + 1

        print()


def printN():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (j == height):
                print("*", end="")
            elif (j == counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter + 1
        print()


def printO():
    space = height // 3
    width = height // 2 + height // 5 + space + space
    for i in range(0, height):
        for j in range(0, width + 1):
            if (j == width - abs(space) or j == abs(space)):
                print("*", end="")
            elif ((i == 0 or i == height - 1) and j > abs(space) and j < width - abs(space)):
                print("*", end="")
            else:
                print(end=" ")

        if (space != 0 and i < height // 2):
            space = space - 1
        elif (i >= (height // 2 + height // 5)):
            space = space - 1

        print()


def printP():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height // 2) and j < height - 1):
                print("*", end="")
            elif (i < height // 2 and j == height - 1 and i != 0):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printQ():
    printO()
    d = height
    for i in range(0, height//2):
        for j in range(0, d+1):
            if (j == d):
                print("*", end="")
            else:
                print(end=" ")
        print()
        d = d+1


def printR():
    half = (height // 2)
    for i in range(0, height):
        print("*", end="")
        for j in range(0, width):
            if ((i == 0 or i == half) and j < (width - 2)):
                print("*", end="")
            elif (j == (width - 2) and not (i == 0 or i == half)):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printS():
    for i in range(0, height):
        for j in range(0, height):
            if ((i == 0 or i == height // 2 or i == height - 1)):
                print("*", end="")
            elif (i < height // 2 and j == 0):
                print("*", end="")
            elif (i > height // 2 and j == height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printT():
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printU():
    for i in range(0, height):
        if (i != 0 and i != height - 1):
            print("*", end="")
        else:
            print(end=" ")
        for j in range(0, height):
            if (((i == height - 1) and j >= 0 and j < height - 1)):
                print("*", end="")
            elif (j == height - 1 and i != 0 and i != height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


def printV():
    counter = 0
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == counter or j == width - counter - 1):
                print("*", end="")
            else:
                print(end=" ")

        counter = counter + 1
        print()


def printW():
    counter = height // 2
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height+1):
            if (j == height):
                print("*", end="")
            elif ((i >= height // 2) and (j == counter or j == height - counter - 1)):
                print("*", end="")
            else:
                print(end=" ")
        if (i >= height // 2):
            counter = counter + 1
        print()


def printX():
    counter = 0
    for i in range(0, height+1):
        for j in range(0, height+1):
            if (j == counter or j == height - counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter + 1
        print()


def printY():
    counter = 0
    for i in range(0, height):
        for j in range(0, height+1):
            if (j == counter or j == height - counter and i <= height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()
        if (i < height // 2):
            counter = counter + 1


def printZ():
    counter = height - 1
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1 or j == counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter - 1
        print()

def error():
    print("You have Entered a number or a symbol, which is not supported right now. Please Enter Alphabets\n")
       

def printLetters(character):

    if character == 'A ' or character == 'a':
        return printA()
    elif character == 'B' or character == 'b':
        return printB()
    elif character == 'C' or character == 'c':
        return printC()
    elif character == 'D' or character == 'd':
        return printD()
    elif character == 'E' or character == 'e':
        return printE(),
    elif character == 'F' or character == 'f':
        return printF(),
    elif character == 'G' or character == 'g':
        return printG(),
    elif character == 'H' or character == 'h':
        return printH(),
    elif character == 'I' or character == 'i':
        return printI(),
    elif character == 'J' or character == 'j':
        return printJ(),
    elif character == 'K' or character == 'k':
        return printK(),
    elif character == 'L' or character == 'l':
        return printL(),
    elif character == 'M' or character == 'm':
        return printM(),
    elif character == 'N' or character == 'n':
        return printN(),
    elif character == 'O' or character == 'o':
        return printO(),
    elif character == 'P' or character == 'p':
        return printP(),
    elif character == 'Q' or character == 'q':
        return printQ(),
    elif character == 'R' or character == 'r':
        return printR(),
    elif character == 'S' or character == 's':
        return printS(),
    elif character == 'T' or character == 't':
        return printT(),
    elif character == 'U' or character == 'u':
        return printU(),
    elif character == 'V' or character == 'v':
        return printV(),
    elif character == 'W' or character == 'w':
        return printW(),
    elif character == 'X' or character == 'x':
        return printX(),
    elif character == 'Y' or character == 'y':
        return printY()
    elif character == 'Z' or character == 'z':
        return printZ()
    else:
        error()


if __name__ == "__main__":
    print("*******************************************************\n")
    print("Let's make Letters with Stars!!\n")
    print("\n*******************************************************\n")
    word = input('Write the Word that you want to Print:-\t')
    for i in word:
        print("\n")
        printLetters(i)
    while True:
        print("*******************************************************\n")
        exit = input("Press 1 to continue and 0 to Exit:-\t")
        print("\n*******************************************************\n")
        if (exit == "1"):
            if __name__ == "__main__":
                word = input('Write the Word that you want to Print:-\t')
            for i in word:
                print("\n")
                printLetters(i)
            
        else:
            break
