año=int(input("escriba el año el cual quiere saber si es bisiesto"))
def año_bisiesto(numero):
  if numero%4!=0:
    print("no es bisiesto")
  elif numero%4 == 0 and numero% 100 !=0:
    print("es bisiesto")
  elif numero%4 == 0 and numero % 100 == 0 and numero % 400 != 0:
    print("no es bisiesto")
  elif numero%4 == 0 and numero % 100 == 0 and numero % 400 == 0:
    print ("es bisisesto")

año_bisiesto(año)