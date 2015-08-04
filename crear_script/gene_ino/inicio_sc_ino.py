#!/usr/bin/python
# -*- coding:utf-8 -*-

def inicio_sc_ino(num):
	
	arduino_ino = open('arduino_script'+num+'.ino','w')
	arduino_ino.write(""" 

/*Sólo para sensores analógicos y es necesarios modificar*/

String etiqueta[] = {
""")
	arduino_ino.close()
