print("classo3")

mountains: list[str] = ["K2","Everest","Nanga Parbat","Himalaya"]
print(mountains)
print(sorted(mountains))
print(mountains.pop())
mountains[0] = "Karakoram"
print(mountains)
mountains.reverse()
print(mountains)
mountains.sort()
print(mountains)
mountains.append("Himalaya")
print(mountains)
mountains.insert(0,"Hindukush")
print(mountains)
mountains.remove("Himalaya")
print(mountains)
mountains2: list[str] = ["K2","Himalaya","Tirich Mir"]
mountains.extend(mountains2)
print(mountains)