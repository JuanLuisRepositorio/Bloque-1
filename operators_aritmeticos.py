#Ejemplo 11
#operadores aritmeticos
#suma, multiplicacion y division pueden usarse con numeros
number = 3 + 2 * 3 / 4.0
print(number)

#se pueden anadir parentesis para que unas operaciones se realicen antes que otras
number = (3 + 2) * 3 / 4.0
print(number)

#operador modulo devuelve la parte entera de una division
remainder = 11 % 3
print(remainder)

#el uso de la doble multiplicacion nos permite calcular potentcias
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#anadir y asignar
a=2
a+=2
print(a)

#Operar con cadenas
#Podemos usar el caracter + para anadir una cadena a otra:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

#Tambien podemos usarlo para juntar variables y cadenas:
x = "awesome"
print("Python is " + x)

#Mezclando operadores entre los numeros y cadenas que no son soportadas:
# Esto no funcionará!
x=1
y=3
print (x + y + "hola")

#la forma correcta seria pasar las variables de tipo numerico a cadenas
x=1
y=3
print (str(x) + str(y) + "hola")

