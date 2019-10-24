#ejercicio 1

#anade a la lista de cadenas las palabras "orange", "apple" y "banana" en este orden y elimina el elmento "audi"

lista = ["lemon","audi"]

#Codigo de comprobacion
a = 20
if (lista[0] == "lemon")and(lista[1]=="orange")and(lista[2]=="apple")and(lista[3]=="banana"):
  a = 1
elif(lista[0] == "lemon")and(lista[1]=="orange")and(lista[2]=="apple")and(lista[3]=="banana"):
  a = 2
elif(lista[0] == "lemon")and(lista[1]=="orange")and(lista[2]=="apple")and(lista[3]=="banana"):
  a = 3
elif(lista[0] == "lemon")and(lista[1]=="orange")and(lista[0]=="apple")and(lista[3]=="banana"):
  a = 4

print("El resultado final para el formulario es: " + str(a))
