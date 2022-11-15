filename = "L09T01.txt"
file = open(filename, "r")
result = file.read()
print(result)
file.close()

sukunimet = result.split(", ")

sukunimet.sort()

snimi = [str(element) for element in sukunimet]
snimet = ", ".join(snimi)

print(snimet)

