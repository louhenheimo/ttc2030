luku = int(input("Montako lukua: "))
laskuri = 1
luvut=[]

for x in list(range(0,luku)):
    z=10*x
    luvut += [z]

for y in range(len(luvut)):
    print(laskuri," luku: ",sep=".",end="")
    print(luvut[y])
    laskuri+=1