print(" este programa  muestra las tablas de multiplicar del 1 hasta el 10")
tabla =[1,2,3,4,5,6,7,8,9,10]
def multiplicacion (una_tabla):
  for i in una_tabla:
    for j in una_tabla:
      operacion = i*j
      print(i,"*",j, "=",operacion)

multiplicacion(tabla)

