granos=0
for i in range(8*8):
  granos+=2**i
  print(i,granos)
print(" el total es: %E granos de trigo." % (granos))