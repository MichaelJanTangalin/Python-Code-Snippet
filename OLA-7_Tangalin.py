# Tangalin, Michael Jan R.
# 3BSIT-2(Online)
# OLA # 7

import sys


def createHeader():
    with open("record.txt", "a") as create:
        with open("record.txt", "r") as countRecordHeader:
            countLine = len(countRecordHeader.readlines()[1:])
            if countLine == 0:
                create.write(f"{'Name:':{20}} {'Email Address:':{25}} {'Address:':{17}}\n")


while True:

    try:
        file = open("record.txt", "r")
    except FileNotFoundError:
        file = open("record.txt", "x")

    print("\nRECORD KEEPING APP")
    print(" A. Add a record" +
          "\n B. View all record" +
          "\n C. Clear all records" +
          "\n D. Exit")
    choice = input("Please enter your choice: ")

    if choice.upper() == 'A'.upper():
        createHeader()
        file = open("record.txt", "a+")
        varName = input(" Name: ")
        varEmail = input(" Email Address: ")
        varAdd = input(" Home Address: ")
        print("\nRecord has been Created!")
        file.write(f"{varName:{20}} {varEmail:{25}} {varAdd:{17}}\n")

    elif choice.upper() == 'B'.upper():
        with open("record.txt", "r") as countRecords:
            count = len(countRecords.readlines()[1:])
            if count == 0:
                print("\nRecords Empty!")
            else:
                file = open("record.txt", "r")
                record = file.read()
                print(record)
                file.close()

    elif choice.upper() == 'C'.upper():
        file = open("record.txt", "r+")
        file.truncate(0)
        print("\nNo records found!")

    elif choice.upper() == "D":
        sys.exit("\nThank you!")

    else:
        print("Invalid input Try Again\n")
