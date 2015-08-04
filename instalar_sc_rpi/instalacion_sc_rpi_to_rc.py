#!/usr/bin/python
# -*- coding:utf-8 -*-

#intalacion del script en rc.local, darle permisos de ejecución y lanzarlo

import os, sys, re

def instalacion_sc_rpi_to_rc():

	machines = []

	listinst = os.listdir('.')

	listinst.sort()

	for i in listinst:
		promach = re.match('actualizar_sensores.+',i)
		if not promach == None:
			machines.append(i)

	for i in machines:

		os.chmod(i, 457) #permisos de ejecución

		try:
			rc = open('/etc/rc.local','r')
		except:
			print "Es necesario ser Root para realizar esta acción"
			sys.exit(1)

		text = rc.readlines()

		rc.close()

		try:
			rca = open('/etc/rc.local','w')
		except:
			print "/etc/rc.local no puede abrir para escritura -- Necesita permisos ROOT"

		text.insert(len(text)-1, os.getcwd()+'/'+i+'\n')
		text.insert(len(text)-1, '\n')

		for i in text:
			rca.write(i)

		rca.close()

	print chr(27)+'[1;35m\nInstalado correctamente, ahora es necesario reiniciar para que la instalación tenga efecto'+chr(27)+'[0m'

	#actulizar_sensores.py

#prueba
#instalacion_sc_rpi_to_rc()
