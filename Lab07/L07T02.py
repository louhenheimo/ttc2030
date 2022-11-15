class Human:
    name = ""
    age = 0
    def __str__(self):
        return "Nimi: " + self.name + ", ikä: " + " " + str(self.age)

adam = Human()
adam.name = "Adam"
adam.age = "19"

eva = Human()
eva.name = "Eva"
eva.age = "18"


print(adam)
print(eva)