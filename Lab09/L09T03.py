luvut = []
laskuri = 0
luku = 0

luku = input("Anna kokonaisluku (tyhjä syöte lopettaa): ")

while luku:
        laskuri += 1
        luvut.append(luku)
        luku = input("Anna kokonaisluku (tyhjä syöte lopettaa): ")

for i in range(len(luvut)):
    luvut[i] = int(luvut [i])

laskuri = str(laskuri)

loppu = str(". Syötetty " + laskuri + " lukua." + "\n")

sluku = [str(element) for element in luvut]
sluvut = ", ".join(sluku)

sluvut = sluvut + loppu

print(sluvut)

filename = "luvut.txt"
try:
    file = open(filename, "w")
    file.write(sluvut)
    file.close()
except:
    print("Virhe tapahtui")
