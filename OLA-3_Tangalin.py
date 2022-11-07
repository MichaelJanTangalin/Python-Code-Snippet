# Tangalin, Michael Jan R.
# 3BSIT-2(Online)
# OLA # 3

employeeName = input("Enter employee name: ")
yearsOfService = input("Enter years-in-service: ")
office = input("Enter office: ")
bonus = 0

if str.upper(office) == "IT":

    if int(yearsOfService) >= 10:
        bonus = 10000

    elif int(yearsOfService) < 10:
        bonus = 5000

elif str.upper(office) == "ACCT":

    if int(yearsOfService) >= 10:
        bonus = 12000

    elif int(yearsOfService) < 10:
        bonus = 6000

elif str.upper(office) == "HR":

    if int(yearsOfService) >= 10:
        bonus = 15000

    elif int(yearsOfService) < 10:
        bonus = 7500

else:

    print("\nInvalid Office")
    exit()

print("Hi " + str(employeeName) + ", your bonus is " + str(int(bonus)) +
".")