#!/usr/bin/python
# -*- coding:utf-8 -*-

# Esta función se encarga de crear sensores y actuadores --> Dummy en Domoticz

#usage: crear_sensor_act('name:passwd@10.0.0.2:8080','246')

import urllib2, sys, json, re, os, random, glob, time
from string import ascii_letters

def id_generator(): 
	return ''.join(random.choice(ascii_letters) for _ in range(8))

def crear_sensor_act (direccion, tipo):

	conv_sen_act = {'249':'Calidad del Aire', '7':'Alerta', '113':'Contador', '9':'Amperimetro', '90':'Contador electrico', '3':'Gas', '81':'Humedad', '246':'Luz', '2':'Porcentaje', '1':'Presion', '85':'Lluvia', '6':'Interruptor', '80':'Temperatura', '82':'Temp+Hum', '84':'Temp+Hum+Pres', '5':'Texto', '248':'Uso electrico', '87':'Intensidad de luz UV', '4':'Voltaje', '86':'Viento' }

#definición de nombres de sensores

	posible = None
	nombreHardware = None
	nombresensor = None

        while nombresensor == None or nombresensor == '' or not posible == None:
                nombresensor = raw_input('Nombre para el sensor de '+conv_sen_act[tipo]+' > ')
                posible = re.match('\s.+|.+\s', nombresensor)

	while nombreHardware == None or nombreHardware == '' or not posible == None:
		nombreHardware = nombresensor+'_HW'
		posible = re.match('\s.+|.+\s', nombreHardware)

	num = 0

	arduinosmatutinos = glob.glob('/dev/ttyACM*')

	continuar = False
	
	lista_numeros = dict()

	for i in arduinosmatutinos:
		num += 1
		lista_numeros.update({i:str(num)})
	
	while continuar !=True:

		for i in lista_numeros:
			print  i,':',lista_numeros[i]
			

		arduinonum = raw_input('Interfaz de Arduino para el sensor '+nombresensor+' (Default: 1) > ')

		if arduinonum == '':
			arduinonum = '1'

		if arduinonum in lista_numeros.values():
			continuar = True
		else:
			print 'Mala elección, elija de nuevo'

#Incorporación del dispositivo deseado en el sistema

	se_puede = 0

	while se_puede == 0:
		try:
			se_puede = 1
			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=getSunRiseSet')
		except:
			print 'Reiniciando domoticz (Se necesita ser ROOT)'
			os.system('/etc/init.d/domoticz.sh restart')
			se_puede = 0
			time.sleep(2)
	
	try:
		urllib2.urlopen('http://'+ direccion+'/json.htm?type=command&param=addhardware&htype=15&port=1&name='+nombreHardware+'&enabled=true&datatimeout=0')

		hardw = urllib2.urlopen('http://'+ direccion +'/json.htm?type=hardware')

		datahw = json.loads(hardw.read())

		idxhw = datahw['result'][len(datahw['result'])-1]['idx']

		urllib2.urlopen('http://'+ direccion +'/json.htm?type=createvirtualsensor&idx='+idxhw+'&sensortype='+tipo)

		sensor = urllib2.urlopen('http://'+ direccion +'/json.htm?type=devices&filter=all&order=Name')

		datasensor = json.loads(sensor.read())

		idxsen = datasensor['result'][len(datasensor['result'])-1]['idx']

		urllib2.urlopen('http://'+ direccion +'/json.htm?type=setused&idx='+idxsen+'&name='+nombresensor+'&used=true')

	except:
		print "El sensor/actuador con id "+nombresensor+" no se ha podido crear."
		print "Compruebe la dirección IP y el puerto."
		print "Si no se soluciona el problema, comuniquelo al soporte técnico."
		sys.exit(1)

#Escribir datos del archivo creado para crear el archivo de automatización de lectura para arduino --> scrip de configuración

	try:
		if arduinonum == '1':
			fichero = open('sensores_creados.txt','a')
			fichero.writelines(nombresensor+' '+idxsen+' '+tipo+'\n')
			fichero.close()
		else:
                        fichero = open('sensores_creados'+arduinonum+'.txt','a')
                        fichero.writelines(nombresensor+' '+idxsen+' '+tipo+'\n')
                        fichero.close()

	except IOError:
		print "No se ha podido escribir el idx del sensor en el fichero.\nIntentelo de nuevo y comuniquelo al soporte técnico"
		fichero.close()
		sys.exit(1)


#prueba de SVN
#crear_sensor_act('10.0.0.2:8080','246')	
