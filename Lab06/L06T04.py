luku1 = int(input("Hypyn pisteet: "))
luku2 = int(input("Hypyn pisteet: "))
luku3 = int(input("Hypyn pisteet: "))
luku4 = int(input("Hypyn pisteet: "))
luku5 = int(input("Hypyn pisteet: "))

summa = 0

luvut = [luku1,luku2,luku3,luku4,luku5]
luvut.sort()
del luvut[4]
del luvut[0]


for i in luvut:
    
        summa += i

print("Pisteet yhteensä:",summa)