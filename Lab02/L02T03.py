from re import I


nimi = input("Anna nimesi: ")

i = nimi.find(' ')

print("Etunimesi: ",nimi[:i] )
print("Sukunimesi: ",nimi[i:] )
