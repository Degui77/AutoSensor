#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys, re, urllib2, serial, glob, shutil

from instalar_sc_ino.flaseo_ino.compile_ino import compile_ino  
from instalar_sc_ino.flaseo_ino.flaseo_ino import flaseo_ino


def instalacion_sc_to_ino():

	currentdir = os.getcwd()

        lista_ino = glob.glob('*.ino')

	if len(lista_ino) == 0:
		print chr(27)+'[1;32mNo hay ningún fichero para Arduino'+chr(27)+'[0m'
		return

	elif len(lista_ino) == 1:
		print 'El fichero que se utilizará es',lista_ino[0]
		
		ficheroObj = lista_ino[0] 		

	else:
        	contador_fichero = 0

		elecciones = {}

		for i in lista_ino:
		
			contador_fichero += 1
		
			elecciones.update({contador_fichero:i})

		print '\nFicheros disponibles:'

		eleccion = None

		while eleccion == None:

	        	for i,j in elecciones.items():

				print i,':',j		

			eleccion = raw_input("\nQué fichero quieres compilar? (ej. 1) > ")

		ficheroObj = elecciones[int(eleccion)]

	dirname = compile_ino(ficheroObj)

	#Nota. El direcctiorio se cambia cuando termina la función anterior (OJO, TENLO EN CUENTA)

	if flaseo_ino(dirname) == 1:
		
		print 'No se ha flaseado Arduino por un error de compilación'

	os.chdir(currentdir)
	shutil.rmtree(dirname)        
	


#instalacion_sc_to_ino()
