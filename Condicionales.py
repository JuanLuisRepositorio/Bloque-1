#Python hace uso de variables booleanas para evaluar condiciones. Cuando una expresión es comparada o evaluada los valores que boleanos que se retorna son falso o verdadero. Por ejemplo:

x = 2
print x == 2 # Imprimira en pantalla TRUE
print x == 3 # Imprimira en pantalla FALSE
print x < 3  # Imprimira en pantalla TRUE
#Nota: para asignar valores a una variable se utiliza el operador de igualdad "=", mientras que para comprar las variables entre ellas se hace uso de dos signos de igualdad "==". La no igualdad se realiza con el operador "!="

#Operadores boleanos
#Los operadores boleanos "y " (and) y "o " (or) permite construir complejas expresiones boleanas, por ejemplo:

name = "John"
age = 23
if name == "John" and age == 23:
    print "tu nombre es John, y tu tienes 23 años."

if name == "John" or name == "Rick":
    print "Tu nombre es John o puede ser  Rick."
#El operador "in"
#El operador "in" puede ser usado para checar si un objeto especifico existe mientras el mismo objeto itera en un contenedor, tanto com una lista:

if name in ["John", "Rick"]:
    print "Su nombre puede ser John or Rick."
#Python usa indentacion para definir bloques de código, en lugar de llaves o paréntesis. El estandar de indentacion de python es 4 espacios, aunque el tab y algunos otros espacios funcionará, siempre y cuando sean consistente, es decir tengan el mismo tipo de sangrado (separación). Los bloques de código no necesitan de una terminación.

#Por ejemplo:

x = 2
if x == 2:
    print "x igual dos!"
else:
    print "x no es igual a dos."
#Una declaración es evaluada como verdadera, si solo su iteración o flujo es correcta: - El resultado verdadero de una variable booleana se obtiene, o se calcula utilizando una expresión, como una compración aritmética. - Un objeto que no es considerado vacío es pasado. - An object which is not considered "empty" is passed.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Se presenta algunos ejemplos donde los objetos son considerados como vacíos:

Una Cadena vacia: ""
Una lista vacia: []
El numero cero: 0
La variable boelana falsa: False
El operador "is"
A diferencia del doble operador de igualdad "==", el operador "is" no sola iguala los valores de las varialbes, si no entre ellos. Por ejemplo

x = [1,2,3]
y = [1,2,3]
print x == y # Imprime en pantalla TRUE
print x is y # Imprime en pantalla FALSE
El operador "not"
Usando "not" delante de una expresión booleana se invierte:

print not False # Imprime en pantalla TRUE
print (not False) == (False) # Imprime en pantalla FALSE
