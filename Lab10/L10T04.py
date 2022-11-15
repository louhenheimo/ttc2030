lista = [0,1,2,3]

muutos = int(input("Mikä luku laitetaan olemattomaan indeksiin: "))

try:
    lista[4] = muutos
except:
    print("Eihän sellainen onnistu!")