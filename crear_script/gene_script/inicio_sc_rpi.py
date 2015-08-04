#!/usr/bin/python
# -*- coding:utf-8 -*-

def inicio_sc_rpi(dispositivo, rbate, num):

	script_f = open('actualizar_sensores'+str(num)+'.py','w')
	script_f.write("""#!/usr/bin/python
# -*- coding:utf-8 -*-

### Importante tener instalado python-serial, python-time, python-urllib2, python-syslog, python-os

import serial
import time
import urllib2
import syslog
import os
import re

puerto = serial.Serial('"""+dispositivo+"""',"""+rbate+""",timeout=1)

def serial_url_used(sstr, direccion, idx, tipo, msg1, msg2):

        tiposval2 = '87', '90'
        tiponval = '1', '2', '81'

	puerto.write(sstr+'\\n')

	rstr = puerto.readline()	
	
        rstv = re.match('(.+)\\n$',rstr) 

        rstr = rstv.group(1)

	try:

		if tipo in tiposval2:
	
			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=udevice&idx='+idx+'&nvalue=0&svalue=' + rstr + ';' + rstr)			
	
		elif tipo in tiponval:

			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=udevice&idx='+idx+'&nvalue='+rstr+'&svalue='+rstr)

		elif tipo == '6':

			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=switchlight&idx='+idx+'&switchcmd='+rstr+'&level=0')

		elif tipo == '82':

                	status = [3,0,2,1]
			position = 0

			tmp_hum = re.match('(.+);(.+)',rstr)

			for hum in range(25,75,25):
				if hum > int(float(tmp_hum.group(2))):
					position += 1

			if position == 1 and float(tmp_hum.group(1)) >= 18.0 and float(tmp_hum.group(1)) <= 22.0:
				position = 3

			rstr = rstr+';'+str(status[position])

			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=udevice&idx='+idx+'&nvalue=0&svalue='+rstr)

		elif tipo == '7':

                	if rstr == '1':
				tone = 3
				rstr = msg1
			else:
				tone = 1
				rstr = msg2

			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=udevice&idx='+idx+'&nvalue='+str(tone)+'&svalue='+rstr)
		
		else:
			urllib2.urlopen('http://'+direccion+'/json.htm?type=command&param=udevice&idx='+idx+'&nvalue=0&svalue=' + rstr)

	except:
		syslog.syslog(syslog.LOG_ERR, 'Error al actualizar dispositivo --> reiniciar domoticz')
		syslog.syslog(syslog.LOG_ERR, 'Reiniciando domoticz')
		os.system('/etc/init.d/domoticz.sh restart')


while True:
	try:
""")

	script_f.close()
