#!/usr/bin/python
# -*- coding:utf-8 -*-

def anadefin_sc_ino(num):
	arduino_ino = open('arduino_script.ino','a')
	arduino_ino.write(""" 
}; //etiquetas --> campo "nombre"

int nsenact = """+str(num)+""";
""")
	arduino_ino.close()
