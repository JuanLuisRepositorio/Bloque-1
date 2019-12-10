#Siendo a y b parametros de entrada
# crea un módulo con las siguientes funciones: suma, resta, divide, multiplica y raiz. Cada una de ellas calculan respectivamente la suma de a mas b, la resta de a menos b, la division de a entre b, la multiplicacion de a por b y por ultimo la raiz de a. Después ejecuta el código, copia el numero que aparece en la consola y sus tres primeros decimales (hasta las milesimas Ejemplo: 120.456) pon este resultado en la pregunta que corresponda en microsoft forms
import calculadora


'''
NO TOCAR
'''

a = 8
b = 2

resultado = math.lgamma(calculadora.suma(a, b) + calculadora.resta(a, b) + calculadora.multiplica(a, b) + calculadora.divide(a, b) + calculadora.raiz(a))

print(resultado)