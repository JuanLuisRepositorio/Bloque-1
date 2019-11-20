#Ejemplo 5
import statistics

importes = [10,201,345,123,345.56,32.3,19.3,235,98,78]

media = statistics.mean(importes)
mediana = statistics.median(importes)
desviacion_estandar = statistics.stdev(importes)

print("Nuestros resultados son:\n media: "+ str(media)  +"\n mediana: " + str(mediana) + "\ndesviacion estandar: " + str(desviacion_estandar))
