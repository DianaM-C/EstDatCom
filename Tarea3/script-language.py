import TRAD.ESP
import TRAD.ENG
import TRAD.JAP

print('''
         >>> ○ <<<
╔════════════════════════╗
║  Podemos saludarlo en  ║
╠════════════════════════╣
║      1.- Español       ║
║      2.- Inglés        ║
║      3.- Japonés       ║
╠════════════════════════╣
║      4.- Salir         ║
╚════════════════════════╝
         >>> ○ <<<
''')

switch = True

try:
    while switch:
        opc = int(input('Por favor ingrese el número de la opción\nseleccionada y obtenga su saludo :)\n ► '))

        if opc == 4:
            switch = False

        elif opc == 1:
            TRAD.ESP.saludo()

        elif opc == 2:
            TRAD.ENG.saludo()

        elif opc == 3:
            TRAD.JAP.saludo()

        else:
            print('\n>>> Opción inexistente <<<\n')

    print('\n>>> Fin del programa <<<\n')

except ValueError:
    print('\n>>> Ingrese el valor en números enteros, gracias <<<')