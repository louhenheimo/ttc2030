luku1 = int(input("Anna 1.luku: "))
luku2 = int(input("Anna 2.luku: "))
luku3 = int(input("Anna 3.luku: "))
luku4 = int(input("Anna 4.luku: "))
luku5 = int(input("Anna 5.luku: "))

summa = 0

luvut = [luku1,luku2,luku3,luku4,luku5]

for i in luvut:
    if i >= 0:
        summa += i

print("Lukujen summa on:",summa)