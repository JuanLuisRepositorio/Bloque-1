#Ejemplo 1
edad = int(input("Escriba su edad: "))

#Comprobacion acceso por edad al contenido A
if edad >= 18:
    print("Ha accedido correctamente al contenido")
  
    
#Ejemplo 2
#Comprobacion acceso por edad al contenido B
edad = int(input("Escriba su edad: "))
nombre = input("Escriba su nombre: ")
age = 23
if nombre == "Juan" and edad >= 18:
    print ("Ha accedido correctamente al contenido 'A'")

#Comprobacion acceso por edad al contenido C

if nombre == "John" or nombre == "Ana":
    print ("Ha accedido correctamente al contenido 'B'")

    
#Ejemplo 3
x = 3
if x == 2:
    print ("x igual dos!")
else:
    print ("x no es igual a dos.")
#Una declaración es evaluada como verdadera, si solo su iteración o flujo es correcta: - El resultado verdadero de una variable booleana se obtiene, o se calcula utilizando una expresión, como una compración aritmética. - Un objeto que no es considerado vacío es pasado. - An object which is not considered "empty" is passed.

#Ejemplo 4
#You can have if statements inside if statements, this is called nested if statements.
x = int(input("Cuantos años tienes: "))
if x > 10:
  print("Más de 10")
  if x > 20:
    print("Más de 20")
  else:
    print("Entre 10 y 20")

#Ejemplo 5
a = 33
b = 33

if b > a:
  print("b es mayor que a")  
else:
  if a == b:
    print("a y b son iguales")


if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")







