dogs = ["Roger", 1, "Syd", True, "Quincy", 7]
dogs[2] = "Beau"

dogs.append("Judah")
dogs.extend(["Judah", 5])
dogs += ["Blah", 6]
dogs.remove("Quincy")

print(dogs)
print(dogs.pop())
print(dogs)
print(dogs[-2])
print(dogs[2:4])
print(dogs[2:])
print(dogs[:4])
print(len(dogs))

items = ["Roger", "Syd", "Quincy", "bob"]
items.insert(2, "Test")
items[1:1] = ["Test1", "Test2"]
print(sorted(items,key=str.lower))
items.sort()
print(items)
items.sort(key=str.lower)
print(items)
