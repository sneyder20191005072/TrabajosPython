import random
y =list(range(1,121))
x = random.choice (y)
print('Numero elegido:', x)
if (x < 10 ):
  print('El numero es menor de 10')
elif (x <50):
  print('El numero esta entre 10-50')
elif (x <100):
  print('El numero esta entre 50-100')
else:
  print('El numero es mayor que 100')