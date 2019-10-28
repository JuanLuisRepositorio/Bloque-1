#Ejemplo 1
#print nos sirve para imprimir la variable o texto que queramos, nos ayuda a conocer el conetenido de las variables o a mostrar resultados
print("Hola mundo")

#Ejemplo 2
#Las cadenas estan definidas con comillas sencillas o compuestas.
micadena_simple = 'Hola'
micadena_doble = "Hola"
print(micadena_simple)
print(micadena_doble)

#La diferencia ente las dos es que usando doble comillas lo hace mas facil de incluir los apostofres (de lo contrario concluirira la cadena si se usa doble comillas)
micadena_comillas = "No te preocupes de los 'apostofres' usando comillas dobles"

print(micadena_comillas)


#Ejemplo 3
#Python soporta dos tipos de números - integrales y numeros de punto flotante. (Tambien soporta numeros complejos, los cuales no se explicarán en este tutorial).
#Para definir un integral, usa la siguiente sintaxis:
myint = 7

#Para definir un numero de punto flotante, debes usar una de las siguientes notaciones:
midecimal = 7.0
midecimal = float(7)

#Ejemplo 4
#booleanos
x = True
y = False
print(x)
print(y)

#Elemplo 5
#borrar variables
x = 120
del x
print(x)

#limpiar variables
x = 120
print(x)
x = None
print("despues de limpiar la variable:" + str(x))

#Elemplo 6
#asingnar multiples variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#cambiar variables de un tipo a otro
#enteros
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)

#realesx = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)

#cadenas
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)

