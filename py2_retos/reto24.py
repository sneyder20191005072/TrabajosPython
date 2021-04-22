print("este programa esta hecho para saber si una palabra es palindromo o no ")
palabra=input("escriba la palabra")

def palindromo (texto):
  if str (texto) == str (texto) [::-1]:
    print("Es palindroma")
  else:
    print("no es palindroma")
  

palindromo(palabra)