name: str = "Hijabie"
print(name)

names: list[str] = ["Muhammad Ahsaan", "Hijabie Rabail", "Riv Khan"]
uinput: str = input("Enter your name: ")
if uinput in names:
    print(uinput, "is in the list")
elif uinput not in names:
    print(uinput, "is not in the list")