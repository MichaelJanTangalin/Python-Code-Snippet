# Tangalin, Michael Jan R.
# 3BSIT-2(Online)
# OLA # 6

def reverseFunction(x):
    return x[::-1]


inputText = input("INPUT: ")
print("STRING: " + inputText)
print(f"REVERSED: {reverseFunction(inputText).upper()} ({len(inputText)} Characters)")
