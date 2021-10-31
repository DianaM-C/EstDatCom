
#todo Los nombres de los métodos deben ir en verbo... Fibonacear XD

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end= ' ')
        a, b = b , a + b
    print()

def fib2(n):
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

fib(100)

#Crea el archivo operación_combinada.py, que permita leer una cadena que representa los cálculos que se deben realizar con el módulo de calculadora. Debe permitir trabajar con tres números como mínimo. Debe imprimir el resultado de la operación
#Ejemplo:
#4+5*10=54
#En caso que se ingrese una cadena que no se puede operar , imprimir un mensaje de error.