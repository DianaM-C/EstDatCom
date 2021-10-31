
#!La programación orientada a objetos busca orden
#!El código debe ser REUTILIZADO

'''Sitema de encomiendas'''
datosEnvia = {'nombre': 'José', 'dni': '34092476', 'celular': '346529475'}
datosRecibe = {'nombre': 'Gloria', 'dni': '34092476', 'celular': '346529475'}

#?| Solicitar datos
datosEnvia['nombre'] = input('Ingrese el nombre del cliente:\n ->')
datosEnvia['dni'] = input('Ingrese el DNI del cliente:\n ->')
datosEnvia['celular'] = input('Ingrese el celular del cliente:\n ->')

datosRecibe['nombre'] = input('Ingrese el nombre del destinatario:\n ->')
datosRecibe['dni'] = input('Ingrese el DNI del destinatario:\n ->')
datosRecibe['celular'] = input('Ingrese el celular del destinatario:\n ->')