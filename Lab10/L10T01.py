saldo = 2000

print("Bank account balance:", saldo, "€")
eurot = int(input("How many euros will be added to the balance? "))
sentit = int(input("How many cents will be added to the balance? "))
saldo = float(saldo+eurot+(sentit/100))
print("Bank account balance:", saldo, "€")
