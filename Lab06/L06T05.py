def show_cm(x):

    if isinstance(x, float):
        sentit = x*2.54
        return print(" %.1f tuumaa on %.2f cm" % (x,sentit))
    else:
        sentit = x*2.54
        return print(" %.1d tuumaa on %.2f cm" % (x,sentit))

show_cm(2)
show_cm(4.5)
show_cm(12)