print (" este programa esta hecho para calcular el indice de masa corporal ")
peso= float(input("escriba su peso (Kg)"))
altura = float (input("escriba su altura(m)"))
def masa_corporal (num,num2):
  respuesta= num/pow(num2,2)
  print ("su indice de masa corporal es " )
  print (respuesta)

masa_corporal(peso,altura)



