#print nos sirve para imprimir la variable o texto que queramos, nos ayuda a conocer el conetenido de las variables o a mostrar resultados
print("Hola mundo")

#Las variables son contenedores para almacenar datos, una variable se crea en el momento en el que le damos un valor
x = 5
y = "John"
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

#Combinar variables
#Podemos usar el caracter + para anadir una variable a otra:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

#Tambien podemos usarlo para juntar variables y caracteres:
x = "awesome"
print("Python is " + x)

#En el caso de variables de tipo numeríco, + seria tratado como un operador matematico:
x = 1
y = 2
z = x + y
print(z)

#Se puede asignar a mas de una variable simultaneamente en la misma linea, como se muestra aquí
a, b = 3, 4

#Mezclando operadores entre los numeros y cadenas que no son soportadas:
# Esto no funcionará!
print (x + y + hola)
