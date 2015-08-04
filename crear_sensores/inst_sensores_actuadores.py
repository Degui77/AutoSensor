#!/usr/bin/python
# -*- coding:utf-8 -*-

#Esta función permitirá crear los sensores que queramos siguiendo las simples indicaciones

#usage: inst_sensores_actuadores('name:passwd@10.0.0.2:8080')

import sys

from crear_sensor_act import *

def inst_sensores_actuadores(direccion):

	sen_act = 'Calidad del Aire', 'Alerta', 'Contador', 'Amperimetro', 'Contador electrico', 'Gas', 'Humedad', 'Luz', 'Porcentaje', 'Presion', 'Lluvia', 'Interruptor', 'Temperatura', 'Temp+Hum', 'Text', 'Uso electrico', 'Intensidad de luz UV', 'Voltaje'

	conv_sen_act = {'Calidad del Aire':'249', 'Alerta':'7', 'Contador':'113', 'Amperimetro':'9', 'Contador electrico':'90', 'Gas':'3', 'Humedad':'81', 'Luz':'246', 'Porcentaje':'2', 'Presion':'1', 'Lluvia':'85', 'Interruptor':'6', 'Temperatura':'80', 'Temp+Hum':'82', 'Texto':'5', 'Uso electrico':'248', 'Intensidad de luz UV':'87', 'Voltaje':'4' }

	print 'Si deseas crear sensores, indica el tipo (Ej. Temperatura)\nSi no sabes el nombre del sensor, escribe: ayuda'
	
	while True:	

		action = raw_input('Qué deseas hacer? > ')

		if action == 'ayuda':
			print 'Los sensores disponibles son:'
			for i in sen_act:
				print i
		
		elif conv_sen_act.get(action):
			num = raw_input('Cuantos sensores quieres? > ')
			print chr(27)+'[1;32mNo utilizar espacios en la designación de nombre\nUtilizar la barra baja (_) como espacio'+chr(27)+'[0m'
			for i in range(int(num)):
				crear_sensor_act(direccion,conv_sen_act[action])
			print chr(27)+'[1;35mSe han creado',num,'sensor/es de',action,chr(27)+'[0m'
			break

		else:
			print 'No es una opcion válida'

#prueba
#inst_sensores_actuadores('10.0.0.2:8080')
