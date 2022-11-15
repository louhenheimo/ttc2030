from random import randint

rivi = []
rivi2 = []

luku = 0
laskuri = 0



def lotto():
    laskuri = 0

    if len(rivi) != 0:
        del rivi[:]
        del rivi2[:]

    for i in range(40):
        laskuri = laskuri+1
        rivi.append(laskuri)

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
    rivitys = rivitys+"\n"
    return (rivitys)

tyhja = ""

frivit = " "

filename = "lotto.txt"
try:
        file = open(filename, "w")
        file.write(tyhja)
        file.close()
except:
        print("Virhe tapahtui")

luku = int(input("Montako lottoriviä arvotaan: "))

for i in range(luku):
    filename = "lotto.txt"
    try:
        file = open(filename, "r")
        frivit = file.read()
        file.close()
    except:
        print("Virhe tapahtui")
    
    try:
        file = open(filename, "w")
        file.write(lotto() + "" + frivit)
        file.close()
    except:
        print("Virhe tapahtui")