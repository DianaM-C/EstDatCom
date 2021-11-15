'''
ESTRUCTURAS DE DATOS COMPUTACIONALES
Evaluación continua 1. Programa 1
────────────────────────────────────
Versión 1: Sin validaciones
'''
print('Ingrese la hora de inicio (horas)')
hora = int(input(' ► '))

print('Ingrese los minutos de inicio (minutos)')
minu = int(input(' ► '))

print('Ingrese la duración del evento (minutos)')
dura = int(input(' ► '))

paso1 = hora * 60           #│ Convertimos la hora del inicio del evento a minutos.
paso2 = paso1 + minu        #│ A esa cantidad, le sumamos los minutos de inicio del evento.
paso3 = paso2 + dura        #│ Una vez obtenido el total de minutos de inicio del evento,
                            #│ agregamos los minutos de duración del mismo.
n = paso3 // 1440           #│ Dividimos ese total entre la cantidadd de minutos contenidos
                            #│ en un día, obteniendo la duración del evento en días.
d = n * (1440)              #│ Convertimos los días de duración del evento a minutos.
paso4 = paso3 - d           #│ Restamos los minutos de duración del evento, menos la cantidad
                            #│ de días en minutos, para que, en caso de que el evento dure
                            #│ varios días, sigamos obteneiendo un valor dentro de las 24 horas.
paso5 = paso4 // 60         #│ Convertimos los minútos de término a horas enteras
paso6 = paso4 % 60          #│ Extraemos los minutos restantes
                            #│ Finalmente, imprimimos los resultados en formato hora

print()
print('Hora de término\n ► {}:{}'.format(paso5, paso6))