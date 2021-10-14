"""
Ejercicio 1
Ingresar tres números e imprimir el mayor
"""

lista = []

def maximo(lista):
    maximo = 0
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

print('Ingrese 3 números: ')

for a in range(3):
    numero = int(input('► '))
    lista.append(numero)

print('El número mayor es:', maximo(lista))