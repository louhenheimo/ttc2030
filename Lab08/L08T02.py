kilvet = []


kilpi = input("Anna rekisterikilpi (tyhjä syöte lopettaa): ")

while kilpi:
        kilvet.append(kilpi)
        kilpi = input("Anna rekisterikilpi (tyhjä syöte lopettaa): ")

kilvet.sort()

skilvet = [str(element) for element in kilvet]


rekkarit = ", ".join(skilvet)

print(rekkarit)
