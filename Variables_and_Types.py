#Números
#Python soporta dos tipos de números - integrales y numeros de punto flotante. (Tambien soporta números complejos, los cuales no se explicarán en este tutorial).

#Para definir un integral, usa la siguiente sintaxis:

myint = 7
#Para definir un número de punto flotante, debes usar una de las siguientes notaciones:

midecimal = 7.0
midecimal = float(7)

#Las cadenas están definidas con comillas sencillas o compuestas.

micadena = 'Hola'
micadena = "Hola"
#La diferencia ente las dos es que usando doble comillas lo hace mas facil de incluir los apostofres (de lo contrario concluirira la cadena si se usa doble comillas)

micadena = "No te preocupes de los 'apostofres' usando comillas dobles"
#There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters. These are beyond the scope of this tutorial, but are covered in the Python documentation.

#To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

#For numbers, the + character works as a mathematical operator:
uno = 1
dos = 2
tres = uno + dos
print(tres)

#You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

hola = "hola"
mundo = "mundo"
holamundo = hola + " " + mundo
#Se puede asignar a mas de una variable simultaneamente en la misma linea, como se muestra aquí

a, b = 3, 4
#Mezclando operadores entre los numeros y cadenas que no son soportadas:

# Esto no funcionará!
print uno + dos + hola
