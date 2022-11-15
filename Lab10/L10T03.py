def karkaus(vuosi):
    if vuosi%400 == 0:
        i2s=str(vuosi)
        return(i2s + " is a leap year!")
    if vuosi%4 != 0 or vuosi%100 == 0:
        i2s=str(vuosi)
        return(i2s + " is not a leap year!")
    else:
        i2s=str(vuosi)
        return(i2s + " is a leap year!")


vuosi = int(input("Insert year: "))

print(karkaus(vuosi))