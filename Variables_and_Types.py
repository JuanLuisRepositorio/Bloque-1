#Las variables son contenedores para almacenar datos, una variable se crea en el momento en el que le damos un valor
x = 5
y = "John"

#print nos sirve para imprimir la variable o texto que queramos, nos ayuda a conocer el conetenido de las variables o a mostrar resultados
print("Hola mundo")
print(x)
print(y)

#Numeros
#Python soporta dos tipos de números - integrales y numeros de punto flotante. (Tambien soporta numeros complejos, los cuales no se explicarán en este tutorial).
#Para definir un integral, usa la siguiente sintaxis:
myint = 7

#Para definir un numero de punto flotante, debes usar una de las siguientes notaciones:
midecimal = 7.0
midecimal = float(7)

#Cadenas
#Las cadenas están definidas con comillas sencillas o compuestas.
micadena = 'Hola'
micadena = "Hola"

#La diferencia ente las dos es que usando doble comillas lo hace mas facil de incluir los apostofres (de lo contrario concluirira la cadena si se usa doble comillas)
micadena = "No te preocupes de los 'apostofres' usando comillas dobles"

#booleanos
x = True
y = False

#borrar variables
x = 120
del x
print(x)

#limpiar variables
x = 120
print(x)
x = None
print("despues de limpiar la variable:" + str(x))

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

#realesx = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#cadenas
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

