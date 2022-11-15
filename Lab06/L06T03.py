laskuri=0

nimet = []

nimi = input("Anna oppilaan nimi: ")

while nimi:
        laskuri += 1
        nimet.append(nimi)
        nimi = input("Anna oppilaan nimi: ")

oppilaat = ", ".join(nimet)
    

print("Oppilaita: ", laskuri)
print(oppilaat)