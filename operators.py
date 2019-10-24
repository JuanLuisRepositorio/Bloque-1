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
