from datetime import date

enimi = input("Anna etunimesi: ")
svuosi = int(input("Anna syntymävuotesi: "))
pvm = date.today()
ika = (pvm.year-svuosi)
print("Hei " + enimi + ", olet ",ika)