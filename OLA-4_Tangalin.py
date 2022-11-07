# Tangalin, Michael Jan R.
# 3BSIT-2(Online)
# OLA # 4

response = "y"
totalWords = list()

while response.upper() == "Y":
    inputWords = str(input("Enter a word: "))
    totalWords.append(inputWords)
    response = str(input("Do you want to try again? [Y/N]: "))

if response.upper() == "N":
    print(f"You entered {len(totalWords)} words")
    for i in totalWords:
        print(i)