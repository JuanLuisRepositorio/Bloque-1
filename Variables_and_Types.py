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
