from typing import Dict

kilvet = []
ks = []
vs = []



class Autot:
    merkki = ""
    kilpi  = ""
    def __str__(self):
        return "Auto: " + self.merkki + " " + self.kilpi
    def __init__(self, merkki, kilpi):
        self.merkki = merkki
        self.kilpi = kilpi


kilvet.append(Autot("Skoda","PCC-546"))
kilvet.append(Autot("Toyota","KBX-652"))
kilvet.append(Autot("Volkswagen","EFV-544"))
kilvet.append(Autot("Volvo","OFR-757"))
kilvet.append(Autot("Kia","MTJ-672"))
kilvet.append(Autot("Ford","QXH-422"))
kilvet.append(Autot("BMW","CAG-464"))
kilvet.append(Autot("Audi","TLR-887"))
kilvet.append(Autot("Hyundai","UIE-278"))
kilvet.append(Autot("Honda","NXX-621"))

for i in range(10):
    #print(kilvet[i].merkki + kilvet[i].kilpi)
    ks.append(kilvet[i].kilpi)
    vs.append(kilvet[i].merkki)

kilvetdct = {}

for i in range(10):
    kilvetdct[ks[i]] = vs[i]

print(dict(sorted(kilvetdct.items())))

#for i in range(9):
#    print(kilvetdct[ks[i]])
