from estructuras import Pila
while True:
    try:
        contenedores1 = Pila.pila()

        print('\nIngrese la cantidad de contenedores que desea apilar')

        while True:
            cantidad = int(input(' ► '))
            if cantidad >= 2:
                break
            else:
                print('\nPor favor ingrese un valor mayor o igual a dos')
                continue

        contenedor = 1

        for i in range(cantidad):
            contenedores1.push(contenedor)
            contenedor += 1

        print('\nContenedores apilados con éxito\n • {}\n'.format(contenedores1.items))

        print('Ingrese el número del contenedor que desea retirar')

        while True:
            retirar = int(input(' ► '))
            if retirar > 0 and retirar <= cantidad:
                break
            else:
                print('\nPor favor ingrese un valor de entre 1 y {}'.format(cantidad))
                continue

        contenedores2 = Pila.pila()

        for i in range(cantidad-retirar):
            sacar = contenedores1.pop()
            contenedores2.push(sacar)

        retirado = contenedores1.pop()

        print('\nContenedor {} retirado con éxito'.format(retirado))

        for i in range(len(contenedores2.items)):
            reponer = contenedores2.pop()
            contenedores1.push(reponer)

        print(' • {}\n\n>>>Fin del programa <<<\n'.format(contenedores1.items))
        break

    except ValueError:
        print('ERROR: Ingrese únicamente valores enteros')
        continue