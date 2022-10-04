summa=0

smaara = []

for i in range(7):
    luku = int(input("Anna sademäärä kokonaislukuna (mm): "))
    smaara.append(luku)

for x in range(len(smaara)):
    summa+=smaara[x]

print("Sademäärä yhteensä: ", summa)
