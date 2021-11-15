'''
ESTRUCTURAS DE DATOS COMPUTACIONALES
Evaluación continua 1: Programa 2
────────────────────────────────────
Versión 1
'''
#│ Profesor disculpe por hacer más de lo que pidió,pero en
#│ la ficha no se especifica sobre si las llamadas deben ser
#│ ingresadas por consola, o desde el propio programa... Así
#│ que hice una versión de cada uno. Espero no sea mucha
#│ molestia que revise ambos.

from Control import movistar, claro, entel, imprimir

print('''
Bienvenido al sistema de control de llamadas

                 >>> ○ <<<
      ╔═════════════════════════════╗
           Operadores registrados
      ╠═════════════════════════════╣
              1.- Movistar
              2.- Claro
              3.- Entel
      ╚═════════════════════════════╝
                 >>> ○ <<<

Ingrese el número del operdor con el cuál se
realizarán las llamadas''')

nume = 947679541
cont = 0
dura = 3

try:
        while True: #│ Para validar que el número que se ingrese
                    #│ es la opción de uno de los operadores existentes.
                opc = int(input(' ► '))

                if opc == 1:
                        opc = movistar
                        name = 'Movistar'
                        break
                elif opc == 2:
                        opc = claro
                        name = 'Claro'
                        break
                elif opc == 3:
                        opc = entel
                        name = 'Entel'
                        break
                else:
                        print('Operador no registrado. Reingresar valor')
                        continue

        for i in range(3): #│ Para ingresar las 3 llamadas solicitadas.
                cont += 1

                if cont == 1:               #│
                        name2 = 'Movistar'  #│
                elif cont == 2:             #│ Para asignar el nombre del operador con
                        name2 = 'Claro'     #│ el cual se realizarán las llamadas.
                elif cont == 3:             #│
                        name2 = 'Entel'     #│

                imprimir.all(opc, nume, dura, cont, name, name2)

                if dura == 5:
                        dura += 10
                dura += 2

        print('Numero al que se llamó: {}'.format(nume), '\n')
        print('          >>> Fin del programa <<<\n')

except ValueError:
        print('Error: Los caracteres ingresados no coinciden con los parámetros establecidos. Ingrese solo valores enteros entre 1 y 3')
        pass

#│ PostData: Tmbn quería preguntarle si sabe la razón por la cual las identaciones
#| se volvieron así de grandes. Creo que sucedió luego de que copié parte de una
#| función del modulo imprimir del paquete Control... Pero no estoy segura. Me
#| gustaría que volvieran a estar como al inicio, es todo. Muchas gracias.