from random import randint

rivi = []
rivi2 = []

laskuri = 0

for i in range(40):
    laskuri = laskuri+1
    rivi.append(laskuri)

def lotto():
    laskuri = 0

    for i in range(7):
        if i == 1:
            nro = (randint(1,39))            
            rivi2.append(rivi[nro-1])
            del rivi[nro-1]
        else:
            nro = (randint(1,39-i))
            rivi2.append(rivi[nro-1])
            del rivi[nro-1]

    rivi2.sort()
    

    srivi = [str(element) for element in rivi2]
    rivitys = ", ".join(srivi)
    return (rivitys)

print(lotto())