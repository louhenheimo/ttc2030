def get_cost(x,y,z):
  return("{:.2f}".format(((x/100)*y)*z) + " €")

print(get_cost(100,7.5,1.88))