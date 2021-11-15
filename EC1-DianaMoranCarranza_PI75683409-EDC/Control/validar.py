from Control import movistar, claro, entel

def opcion():
    while True:
        opc = int(input('Ingrese el número del operador desde el cual se realizó la llamada\n ► '))
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
    return opc, name

def operador():
    while True:
        cont = int(input('Ingrese el número del operador al que se le realizó la llamada\n ► '))
        if cont == 1:
            name2 = 'Movistar'
            break
        elif cont == 2:
            name2 = 'Claro'
            break
        elif cont == 3:
            name2 = 'Entel'
            break
        else:
            print('Operador no registrado')
    return cont, name2