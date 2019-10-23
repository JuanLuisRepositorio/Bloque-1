#Listas son como arreglos flexibles. Estos contienen variables que desees y todas los tipos de variables que esten soportados. Los elementos de la lista pueden ser iterated over! (se explicará mas adelante en el tutorial) o accediendo a ellos via un indice basado en cero.
#crear una lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

#imprimir el segundo elemento de una lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#imprimir el ultimo elemento de una lista
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Accediendo un indice que no exista generará un error.
mylist = [1,2,3]
print (mylist[10])

#imprimir el tercero, cuarto y quinto elemento de una lista
thislist = [1, 2, 3, 4, 5, 6, 7]
print(thislist[2:5])

#cambiar el valor del segundo elemento de una lista
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#append nos permite añadir valores consecutivos a nuestra lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#mediante insert podemos añadir un elemento una lista en una posicion concreta
thislist.insert(2, 'a')
print(thislist)

#eliminar un elemento de la lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#eliminar un elemento de la lista mediante el indice
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#limpiar una lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#unir dos listas
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#el metodo index() busca el indice de un elemento en la lista
my_list = ['a','b','c']
my_list.index('b')




