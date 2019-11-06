#Ejemplo 1
edad = int(input("Escriba su edad: "))
nombre = input("Escriba su nombre: ")

#Comprobacion acceso por edad al contenido A
if edad >= 18:
    print("Ha accedido correctamente al contenido 'A'")


#Comprobacion acceso por edad al contenido B
age = 23
if nombre == "Juan" and edad >= 18:
    print ("Ha accedido correctamente al contenido 'B'")

#Comprobacion acceso por edad al contenido C

if nombre == "John" or nombre == "Ana":
    print ("Ha accedido correctamente al contenido 'C'")

    
#Ejemplo 2

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
