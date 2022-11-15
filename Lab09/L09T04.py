filename = "nimet.txt"
file = open(filename, "r")
result = file.read()
file.close()

nimet = result.split("\n")

#sukunimet.sort()

#snimi = [str(element) for element in sukunimet]
#snimet = ", ".join(snimi)

#nimet = []

#nimet.append(result)

nimet.sort()

nimet2 = []

nimet3 = []

laskuri = 0

for i in range((len(nimet)-1)):
        if nimet[i] == nimet[i+1]:
            laskuri = laskuri+1

for i in range((len(nimet))-1):
        if nimet[i] != nimet[i+1]:
            nimet2.append(nimet[i])

for i in range(len(nimet2)):
    nimet3.append(nimet2[i])


for i in range(laskuri):
    nimetdct =  {nimet2[i]:nimet.count(nimet2[i]) for nimet2[i] in nimet}

for i in range(laskuri):
    print ("Nimi", nimet3[i], "esiintyy", nimetdct.get(nimet3[i]), "kertaa.")
print("Nimiä on yhteensä", len(nimet), "kappaletta.")