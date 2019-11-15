#Ejemplo 3
print("Imprimimos los números de 1 a 10")
for i in range(1, 10):
    print("número: "+ str(i))    


#Ejemplo 4
print("Número de participantes de los cuatro primeros trimestres")
a = 1
for i in [32, 35, 14, 16]:
    print("En el "+ str(a) + "º semestre tenemos "+ str(i) + " participantes")
    a += 1
    
print("¿En que paises tenemos oficinas?")
for i in ["Chile", "Ecuador", "Peru", "Argentina", "España", "Brasil"]:
    print("Tenemos oficina en: "+ str(i))

#Ejemplo 5
#bucle while 1
i = 1
while i <= 3:
    print(i)
    i += 1
print("Programa terminado")

#bucle while 2
i = int(input("introduce numero para empezar el bucle: "))
while i <= 50:
    print(i)
    i += 1
print("Programa terminado")

