# Tangalin, Michael Jan R.
# 3BSIT-2(Online)

StudentName = input("Enter student’s name (LN, FN MI): ")
print("Enter student’s grade in ")
Math = input("\n Math: ")
Science = input(" Science: ")
English = input(" English: ")
Average = (int(Math) + int(Science) + int(English))/3
print("\nAverage grade of " + StudentName + " is " + str(int(Average)))