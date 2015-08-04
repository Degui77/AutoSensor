#!/usr/bin/python
# -*- coding:utf-8 -*-

def fin_sc_rpi(delay, num):

	script_f = open('actualizar_sensores'+str(num)+'.py','a')

	script_f.write("""	except:
		syslog.syslog(syslog.LOG_ERR, 'Error al actualizar dispositivo ')
		continue

	time.sleep("""+delay+""")

""")

	script_f.close()
