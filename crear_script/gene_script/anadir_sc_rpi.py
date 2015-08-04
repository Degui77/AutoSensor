#!/usr/bin/python
# -*- coding:utf-8 -*-

def anadir_sc_rpi(direccion, nombre ,idx, tipo, num, msg1, msg2):

	script_f = open('actualizar_sensores'+str(num)+'.py','a')

	script_f.write("""		serial_url_used('"""+nombre+"""', '"""+direccion+"""', '"""+idx+"""', '"""+tipo+"""', '"""+msg1+"""', '"""+msg2+"""')	

""")

	script_f.close()
