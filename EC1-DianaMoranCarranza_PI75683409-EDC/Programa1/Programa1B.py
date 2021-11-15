'''
ESTRUCTURAS DE DATOS COMPUTACIONALES
Evaluación continua 1. Programa 1
────────────────────────────────────
Versión 2: Validando. Atendiendo errores
'''
while True:
    try:
        print('Ingrese la hora de inicio (horas)')

        while True:
            hora = int(input(' ► '))
            if hora >=0 and hora < 24:
                break
            else:
                print('Por favor ingrese una hora válida (de 0 a 23 horas)')

        print('Ingrese los minutos de inicio (minutos)')
        while True:
            minu = int(input(' ► '))
            if minu >= 0 and minu < 60:
                break
            else:
                print('Por favor ingrese una cantidad válida de minutos (de 0 a 59 minutos)')

        dura = int(input('Ingrese la duración del evento (minutos)\n ► '))
        paso1 = hora * 60
        paso2 = paso1 + minu
        paso3 = paso2 + dura
        n = paso3 // 1440
        d = n * (1440)
        paso4 = paso3 - d
        paso5 = paso4 // 60
        paso6 = paso4 % 60

        print()
        print('Hora de término\n ► {}:{}'.format(paso5, paso6))
        break

    except ValueError:
        print('\nError. Se aceptan unicamente números enteros\n')