class Cat:
    name = ""
    color = ""
    def __str__(self):
        return self.name + ", color: " + self.color
    def miau(self):
        return self.name + " says: Meoooooow!"

kit = Cat()
kit.name = "Kit"
kit.color = "black"

kat = Cat()
kat.name = "Kat"
kat.color = "white"


print(kit)
print(kat)

print(kit.miau())
print(kat.miau())