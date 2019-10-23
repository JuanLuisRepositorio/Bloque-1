#Listas son como arreglos flexibles. Estos contienen variables que desees y todas los tipos de variables que esten soportados. Los elementos de la lista pueden ser iterated over! (se explicará mas adelante en el tutorial) o accediendo a ellos via un indice basado en cero.
#lista de numeros enteros
milista = []
milista.append(10)
milista.append(25)
milista.append(30)
print milista[0] # imprime 10
print milista[1] # imprime 25
print milista[2] # imprime 30

#lista de cadenas de caracteres
milistastring = []
milistastring.append("orange")
milistastring.append("banana")
milistastring.append("apple")
print milistastring[0] # imprime orange
print milistastring[1] # imprime banana
print milistastring[2] # imprime apple

Accediendo un indice que no exista generará un error.

mylist = [1,2,3]
print mylist[10]

