sukunimet = []

sukunimi = input("Anna henkilön sukunimi (tyhjä syöte lopettaa):")

while sukunimi:
        sukunimet.append(sukunimi)
        sukunimi = input("Anna henkilön sukunimi (tyhjä syöte lopettaa):")

snimi = [str(element) for element in sukunimet]
snimet = ", ".join(snimi)

filename = "L09T01.txt"
try:
    file = open(filename, "w")
    file.write(snimet)
    file.close()
except:
    print("Virhe tapahtui")


