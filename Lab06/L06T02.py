def celToFah(x):

    aste = x * 1.8 + 32
    
    return "%0.1f" % (aste)
   
def fahToCel(x):

    aste = (x - 32) / 1.8
    
    return "%0.1f" % (aste)
   

print(celToFah(10.0))
print(fahToCel(38.0))