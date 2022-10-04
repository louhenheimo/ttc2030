enimi = input("Anna etunimi: ")
snimi = input("Anna sukunimi: ")
snimi2 = snimi [::-1]

l=len(enimi)
for x in range(l):
    print(enimi[0],end="")

print(" " + snimi2)