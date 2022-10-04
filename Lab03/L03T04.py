pisteet = int(input("Pisteet: "))
taulu=[0,0,1,1,2,2,3,3,4,4,5,5,5]
if (pisteet >= 0 and pisteet <= 12):
    print("Arvosana:",taulu[pisteet])
else:
    print("Tarkista pistemääräsi.")