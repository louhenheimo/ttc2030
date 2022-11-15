import os.path

ayho = "ayho"
polku = os.path.expanduser("~")
filename = "ayho.txt"
filename2 = polku + "/" + filename
try:
    file = open(filename2, "w")
    file.write(ayho)
    file.close()
    print(filename2 + " luotu onnistuneesti!")
except:
    print("Virhe tapahtui")