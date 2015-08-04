#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys, re, urllib2

from crear_sensores.inst_sensores_actuadores import *
from crear_script.script_ctr_ino import *
from crear_script.script_sensores_act_rpi import *
from instalar_sc_rpi.instalacion_sc_rpi_to_rc import *
from instalar_sc_ino.instalacion_sc_to_ino import *

opcion = "Crear sensores: 1", "Crear script para RPi: 2", "Crear plantilla para Arduino: 3", "Inicio automático de script para Raspberry: 4", "Flasear Arduino: 5" , "Salir: 6"
menu = {'1': inst_sensores_actuadores,
	'2': script_sensores_act_rpi,
	'3': script_ctr_ino,
	'4': instalacion_sc_rpi_to_rc,
	'5': instalacion_sc_to_ino}

print chr(27)+"""[1;32m\n--------------AutoSensor Configuration-------------------
Este progrma permite configurar DomoticZ para el intercambio de
información con los sensores/actuadores conectados a Arduino."""+chr(27)+'[0m'

while True:

	print "\nQué desea hacer?"

	for i in opcion:
		print i

	eleccion = raw_input("\nPulse un número > ")

	if eleccion == '6':
		print chr(27)+"[1;32mFin de la configuración"+chr(27)+'[0m'
		break
	elif menu.get(eleccion):
		if eleccion == '1' or eleccion == '2':

			conf_correcta = 0

        		if len(glob.glob('/dev/ttyACM*')) == 0:
                		print chr(27)+'[1;32mNo se ha detectado Arduino, Conectelo y vuelva a lanzar el programa'+chr(27)+'[0m'
                		sys.exit(1)

			while conf_correcta == 0:

				direccion = raw_input("Direccion, puerto y credenciales (Default: 127.0.0.1:8080) > ")

				if direccion == '':
					direccion = '127.0.0.1:8080'

				if eleccion == '1':
					try:
						urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=getSunRiseSet')					
				
					except:

						print chr(27)+'[1;32mLa dirección es incorrecta\nVuelve a introducirla correctamente\nSi el error permanece reinicia el servidor principal'+chr(27)+'[0m'
					else:

						conf_correcta = 1
				else:
					conf_correcta = 1
			menu[eleccion](direccion)

		else:
			menu[eleccion]()

	else:
		print chr(27)+'[1;32mOpción no válida. Intentelo de nuevo.'+chr(27)+'[0m'


