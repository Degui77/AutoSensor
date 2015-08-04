#!/usr/bin/python
# -*- coding:utf-8 -*-

import re, sys, os

from gene_ino.inicio_sc_ino import *
from gene_ino.anade_sc_ino import *
from gene_ino.anadefin_sc_ino import *
from gene_ino.fin_sc_ino import *

def script_ctr_ino():
	
	num = 0
	
	fichero_sensores = []	

	lista = os.listdir('.')

	lista.sort()

	for i in lista:
		macheados = re.match('sensores_creados.+',i)
		if not macheados == None:
			fichero_sensores.append(i)

	for i  in fichero_sensores:		
		count = 0

		num += 1
	
		try:
			sensores_f = open(i,'r')
		except:
			print 'No se encuentra el fichero con los sensores/actuadores creados'
			print 'Crea los sensores o, si están creados, crea un fichero en la raiz del programa llamado \"sensores_creados.txt\" con el formato intelineado \"<nombre> <idx> <tipo>\"'
			sys.exit(1)

		inicio_sc_ino(str(num))

		while True:
			linea = sensores_f.readline()
			if not linea:
				break
			
			count += 1			
			info = re.match("(.+)\s(.+)\s(.+)", linea)
			etiqueta = info.group(1)

			anade_sc_ino(etiqueta, count, str(num))

		sensores_f.close()

		#anadefin_sc_ino(count, str(num))

		fin_sc_ino(str(num))

		print chr(27)+'[1;35m\nPlantilla para Arduino creada'+chr(27)+'[0m'

#prueba
#script_ctr_ino()

