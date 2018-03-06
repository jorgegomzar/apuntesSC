import os
print('0.- Calcular voltajes.')
print('1.- Calcular potencias.')

opcion = int(input('¿Qué quieres calcular? '))
os.system('cls')
if opcion == 0:
	voltajes = []
	x = 0
	while True:
		nAmp = int(input('Número de amplificadores: '))
		longiud = float(input('Longitud del tramo (km): '))
		resistencia = float(input('Resistencia del lazo (ohm/km): '))
		v = (nAmp * 0.6 * longiud * resistencia)
		voltajes.insert(x, v)
		x = x + 1
		if input('¿Quieres añadir otro tramo? (s/n)').lower() == 'n':
			break
		os.system('cls')
	os.system('cls')
	x = 1
	print('Los voltajes en la línea serían los siguientes:')
	for voltaje in voltajes:
		print('v' + str(x) + ':', format(voltaje, '.2f'), 'voltios')
		x = x + 1
elif opcion == 1:
	while True:
		os.system('cls')
		print('0.- Calcular pérdida de potencia en tramo.')
		print('1.- Calcular pérdida de potencia en TAP.')
		opcion2 = int(input('¿Qué quieres calcular? '))
		os.system('cls')
		if opcion2 == 0:
			perdpormetro = float(input('Pérdida de potencia por metro: '))
			metros = float(input('Distancia en metros del tramo: '))
			entrada = float(input('Potencia al comienzo del tramo: '))
			print('En el final del tramo habrá', format((entrada - (perdpormetro * metros)), '.2f'))
			os.system('pause > nul')
		if opcion2 == 1:
			entrada = float(input('Potencia al comienzo del TAP: '))
			tap = int(input('Pérdida diferencial: '))
			puertos = int(input('Número de puertos: '))
			print('En cada puerto habrá', format(entrada - tap, '.2f'), 'dBu')
			# Incluir aquí una tabla de correspondencias dependiendo del tap y puertos