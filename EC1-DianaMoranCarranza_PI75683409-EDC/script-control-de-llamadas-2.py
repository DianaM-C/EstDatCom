'''
ESTRUCTURAS DE DATOS COMPUTACIONALES
Evaluación continua 1: Programa 2
────────────────────────────────────
Versión 2
'''

from Control import imprimir, validar
print('''
Bienvenido al sistema de control de llamadas
─────────────────────────────────────────────''')
try:
    for i in range(3):
        print('Ingrese el número telefónico')
        while True:
            nume = int(input(' ► '))
            if nume >= 100000000 and nume < 1000000000 :
                break
        dura = float(input('Ingrese la duración de la llamada\n ► '))
        print('')
        print('''Operadores registrados
─────────────────────────────────────────────
 1.- Movistar
 2.- Claro
 3.- Entel
─────────────────────────────────────────────''')

        opc, name = validar.opcion()

        cont, name2 = validar.operador()

        imprimir.all(opc, nume, dura, cont, name, name2)
        print('Numero al que se llamó: {}\n\n'.format(nume))

    print('>>> Fin del programa <<<\n')
except ValueError:
    print('Error: Los caracteres ingresados no coinciden con los parámetros establecidos')