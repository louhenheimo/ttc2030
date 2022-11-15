def kerro3(ika):
    if ika < 13:
        return("child")
    if ika <= 19:
        return("teen")
    if ika <= 65:
        return("adult")
    else:
        return("senior")


ika = int(input("How old are you? "))
print(kerro3(ika))