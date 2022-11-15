arvosanat = []
laskuri = 0
summa = 0
arvosana = 0

arvosana = input("Anna arvosana (tyhjä syöte lopettaa): ")

while arvosana:
        laskuri += 1
        arvosanat.append(arvosana)
        arvosana = input("Anna arvosana (tyhjä syöte lopettaa): ")

for i in range(len(arvosanat)):
    arvosanat[i] = int(arvosanat [i])

for i in range(len(arvosanat)):
    summa += arvosanat [i]

ka = (summa/laskuri)

print("Arvosanoja:", laskuri, "kappaletta, keskiarvo:", ka)
