# Tangalin, Michael Jan R.
# 3BSIT-2(Online)
# OLA # 8

import sys


def createFile():
    with open("record.txt", "w+") as create:
        create.write(f"{'Name:':{25}} {'Email:':{25}} {'Address:':{17}}\n")


try:
    file = open("record.txt", "r")
except FileNotFoundError:
    file = open("record.txt", "x")


class Records:

    def __init__(self, choice):
        self.choice = choice

        if choice.upper() == "A":
            open("record.txt", "r")
            varName = str(input("\nEnter Name: "))
            varEmail = str(input("Enter Email: "))
            varAdd = str(input("Enter Home Address: "))
            print("\nRecord has been Created!\n")
            with open("record.txt", "a") as writeRecord:
                writeRecord.write(f'{varName:{25}} {varEmail:{25}} {varAdd:{17}}\n')

        elif choice.upper() == "B":
            with open("record.txt", "r") as countRecords:
                count = len(countRecords.readlines()[1:])
                if count == 0:
                    print("\nRecords Empty!\n")

                else:
                    with open("record.txt", "r") as readRecords:
                        print(readRecords.read())

        elif choice.upper() == "C":
            print("\nNo records found!\n")
            with open("record.txt", "r+") as clearRec:
                clearRec.truncate(0)

        elif choice.upper() == "D":
            sys.exit("\nThank you!")

        else:
            print("\nInvalid input.\n")


while True:

    with open("record.txt", "r") as cR:
        c = len(cR.readlines())
        if c == 0:
            createFile()

    print("****** Record Keeping App ******")
    print("\n A. Add Record\n B. View Record \n C. Clear Records\n D. Exit App\n")
    selection = str(input("Please Enter your choice: "))
    Records(selection)
