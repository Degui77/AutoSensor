#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, shutil, sys, re, urllib2, serial

from instalar_sc_ino.flaseo_ino.crearSConstruct import crearSConstruct

def compile_ino(fichero_ino):

	nombre_dir_c = re.match('(.+)\.ino',fichero_ino)

	dirname = nombre_dir_c.group(1)

	if not os.path.isdir(os.getcwd()+'/'+dirname):
		os.mkdir(os.getcwd()+'/'+dirname)
	
	shutil.copy(os.getcwd()+'/'+fichero_ino,os.getcwd()+'/'+dirname+'/'+fichero_ino)

	if os.path.isfile(os.getcwd()+'/SConstruct'):
		shutil.copy(os.getcwd()+'/SConstruct',os.getcwd()+'/'+dirname+'/SConstruct')

	else:
		print chr(27)+'[1;32mNo se ha encontrado el fichero SConstruct\nCreandolo..............'+chr(27)+'[0m'

		crearSConstruct(dirname)
	
		print chr(27)+'[1;32mCreado'+chr(27)+'[0m'

	os.chdir(os.getcwd()+'/'+dirname) 
	
	try:
		os.system('/usr/bin/scons')	

	except:	
		print chr(27)+'[1;32mError de compilación\nRevisa el contenido de',fichero_ino,'\no revisa si las librerías se encuentran en: /usr/share/arduino/libraries/<nombre-libreria>/<ficheros-libreria>\n'+chr(27)+'[0m'
		sys.exit(1)

	return dirname
#compile_ino('juan.ino')

