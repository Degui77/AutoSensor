#!/usr/bin/python
# -*- coding:utf-8 -*-

def anade_sc_ino(etiqueta, cont, num):
	arduino_ino = open('arduino_script'+num+'.ino','a')
	if cont == 1:
		arduino_ino.write('"'+etiqueta+'"');
	else:
		arduino_ino.write(', "'+etiqueta+'"');		
	arduino_ino.close()
