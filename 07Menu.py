import os
import sys
def Hello_World():
    print("Hello World")

def Goodbye_World():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def Goodbye_Person():
    print("Hello World")
    name = input("What is your name ? ")
    print("Goodbye "+name)

def Good_Teacher():
    teachername = input("Teacher's name (try Mr Horan) ")
    if teachername == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(teachername+" is an ok teacher")

def forLoop():
    for numbers in range(1, 500):
        print(numbers)

def whileLoop():
    while True:
        subjectname = input("What is the name of this subject ")
        if subjectname == "IST":
            print("")
            print("")
            print(" Congratulations!!")
            print("")
            print("")
            break
        else:
            print("Not Correct - try again")

def endOutput():
    print()
    print("----End of Output -----------------------------")
    print()
    print()
    print()
    input("Press Enter to continue")

while True:
    os.system('cls')
    print(" "+"-"*48)
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Jennica Wang                         |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" "+"-"*48)
    print()
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    userinput = input("Enter an option ")
    print()
    print("----Start of Output ---------------------------")
    print()
    if userinput == ('1'):
        Hello_World()
        endOutput()
        continue
    if userinput == ('2'):
        Goodbye_World()
        endOutput()
        continue
    if userinput == ('3'):
        Goodbye_Person()
        endOutput()
        continue
    if userinput == ('4'):
        Good_Teacher()
        endOutput()
        continue
    if userinput == ('5'):
        forLoop()
        endOutput()
        continue
    if userinput == ('6'):
        whileLoop()
        endOutput()
        continue
    if userinput == ('x'):
        endOutput()
        sys.exit()
    else:
        print("invalid option")
        endOutput()
        continue