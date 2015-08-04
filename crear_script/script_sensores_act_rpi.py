#!/usr/bin/python
# -*- coding:utf-8 -*-

#Esta función permitirá crear el script que controlorá los sensores/actuadores de arduino

#usage: script_sensores_act_rpi('10.0.0.2:8080')

import os, re, sys, glob

from gene_script.inicio_sc_rpi import *
from gene_script.anadir_sc_rpi import *
from gene_script.fin_sc_rpi import *

def script_sensores_act_rpi(direccion):

	
	#ninos = raw_input('¿Cuantos Arduinos quieres? (Default: 1) > ')
	
	ifaces = glob.glob('/dev/ttyACM*')		

	rutaino = []
	brate = []

	for i in range(0, len(ifaces)):

		#rutainor = raw_input('¿Cuál es la ruta del Arduino '+str(i)+'? (Default: /dev/ttyACM0) > ')

		rutainor =  ifaces[i]
			
#		while rutainor in rutaino:
#			rutainor = raw_input('Esta ruta ya existe, escoge otra ruta > ')

#		rutaino.append(rutainor)

		brater = raw_input('¿Cuál es el baudrate para arduino de la interfaz '+rutainor+' ? (Default: 19200) > ')

		if brater == '':
			brater = '19200'

		inicio_sc_rpi(rutainor, brater, i + 1)


		tiempo_delay = raw_input('Cuanto tiempo para actualizar sensores (Default: 4 seg) > ')

		if tiempo_delay == '':
			tiempo_delay = '4'

		try:
			if i == 0:
				sensores_f = open('sensores_creados.txt','r')
			else:
				sensores_f = open('sensores_creados'+str(i+1)+'.txt','r')
		except:
			print 'No se encuentra el fichero con los sensores/actuadores creados'
			print 'Crea los sensores o, si están creados, crea un fichero en la raiz del programa llamado \'sensores_creados.txt\' con el formato intelineado \'<nombre> <idx> <tipo>\''
			sys.exit(1)

		while True:
			linea = sensores_f.readline()

			if not linea:
				break

			info = re.match('(.+)\s(.+)\s(.+)', linea)

			nombre = info.group(1)
			idx = info.group(2)
			tipo = info.group(3)		

			msg1 = ' '
			msg2 = ' '

			if tipo == '7':

				print chr(27)+'[1;32mNo escribir espacios entre las notificaciones'+chr(27)+'[0m'

				posible = '1'

				while msg1 == None or msg1 == '' or not posible == None:
                                	msg1 = raw_input('Notificación mostrada al activarse '+nombre+'> ')
                			posible = re.match('\s.+|.+\s', msg1)

				posible = '1'				

                                while msg2 == None or msg2 == '' or not posible == None:
                                        msg2 = raw_input('Notificación mostrada al desactivarse '+nombre+'> ')
                                        posible = re.match('\s.+|.+\s', msg2)

			anadir_sc_rpi(direccion, nombre, idx, tipo, i+1, msg1, msg2)

		sensores_f.close()

		fin_sc_rpi(tiempo_delay, i+1)

		print chr(27)+'[1;35m\nScript para Raspberry Pi creado'+chr(27)+'[0m'

#prueba
#script_sensores_act_rpi('10.0.0.2:8080')
	
