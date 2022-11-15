def showtime(x):

    tunnit = x//3600
    minuutit = (x-(tunnit*3600))//60
    sekunnit = (x-(tunnit*3600+minuutit*60))
    return "%02d:%02d:%02d" % (tunnit,minuutit,sekunnit)
   

print(showtime(500))