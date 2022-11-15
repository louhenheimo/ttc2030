class Car:
    brand = ""
    model  = ""
    price = 0
    def __str__(self):
        return "Auto: " + self.brand + " " + self.model + " " + str(self.price)
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print(car1)
print(car2)
print(car3)

summa = car1.price + car2.price + car3.price

print("Autojen hinta yhteensä: ", summa)