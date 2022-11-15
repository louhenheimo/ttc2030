nimet = [None] * 10


for i in range(10):
        nimi = input("Anna kaverisi nimi: ")
        nimet[i] = (nimi)

skaverit = [str(element) for element in nimet]

nimet2 = list(reversed(nimet))

skaverit2 = [str(element) for element in nimet2]

kaverit = ", ".join(skaverit)

nurinkaverit =  ", ".join(skaverit2)

print(kaverit)
print(nurinkaverit)
