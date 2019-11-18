#Ejemplo 6
print("Imprimimos los números de 1 a 10")
for i in range(1, 10):
    print("número: "+ str(i))    


#Ejemplo 7
print("Número de participantes de los cuatro primeros trimestres")
a = 1
for numero in [32, 35, 14, 16]:
    print("En el "+ str(a) + "º semestre tenemos "+ str(numero) + " participantes")
    a += 1
    
print("¿En que paises tenemos oficinas?")
for paises in ["Chile", "Ecuador", "Peru", "Argentina", "España", "Brasil"]:
    print("Tenemos oficina en: "+ str(i))

paises = ["Chile", "Ecuador", "Peru", "Argentina", "España", "Brasil"]
for i in range(len(paises)):
    print("Tenemos oficina en: "+ str(paises[i]))    

#Ejemplo 8
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

