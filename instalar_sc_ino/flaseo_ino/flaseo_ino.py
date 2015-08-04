#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys, re, urllib2, serial, glob

def flaseo_ino(dirname):

	puertos = glob.glob('/dev/ttyACM*')

	puerto = ''

	if len(puertos) == 0:
		print chr(27)+'[1;32mNo se encuentra ningún Arduino conectado\nConecte uno y vuelva a ejecutar el programa'+chr(27)+'[0m'
		sys.exit(1)

	elif len(puertos) == 1:
		puerto = puertos[0]
		print 'El puerto de Arduino es:',puerto

	else:
		puertos_dic = {}

		cont_puertos = 0

		passed = 0

		for i in puertos:

                	cont_puertos += 1
			
			puertos_dic.update({cont_puertos:i})

		print 'Selecciona un Arduino:'

		while passed == 0:
			for i,j in puertos_dic.items():

				cont_puertos += 1

				print i,':',j

			eleccion = raw_input('Qué puerto quieres utilizar? > ')

			if int(eleccion) in puertos_dic.key():
				passed = 1
			else:
				print chr(27)+'[1;32mNo se contempla la opción elegida, eliga una opción válida'+chr(27)+'[0m'

		puerto = puertos_dic[int(eleccion)]
	
	ficheros_ar = glob.glob('*.hex')

	if len(ficheros_ar) == 0:
		return 1
	
	flass = '/usr/bin/avrdude -F -c avrisp -b 115200 -p atmega328p -P '+puerto+' -U flash:w:'+dirname+'.hex:i'

	try:
		os.system(flass)
#		print 'FLASED'
	except:
		print chr(27)+'[1;32mError al flasear, revise la instalación de Arduino (apt-get install arduino)'+chr(27)+'[0m'		
				
	print 'Flaseado Arduino....'
	
	return 0
