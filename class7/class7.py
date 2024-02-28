import sys

print("Hello world!")

print("This is the name of the script: ", sys.argv)

while True:
    age = int(input("Enter your age"))
    quit: str = input("Enter quit to exit")
    if age < 3:
        print("The ticket is free")
    elif age >= 3 and age <= 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")