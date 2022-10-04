summa=0
laskuri=0

luku="."

while True:
    try:
        luku = int(input("Anna luku: ")) 
        summa += luku
        laskuri += 1
    except ValueError:
        break
    
    

print("Lukuja annettu: ", laskuri)
print("Lukujen summa: ", summa)