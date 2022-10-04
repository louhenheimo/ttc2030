def get_fuel(x,y):
  return("{:.1f}".format((x/100)*y) + " ltr")

print(get_fuel(100,7.5))