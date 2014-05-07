import platform
import psutil
import datetime
class pymon():
	def _omedida(valor):
		if valor < 1025:
			medida = "Bytes"
		elif valor < 1048577:
			medida = "Kilobytes"
			valor = valor/1024
		elif valor < 1073741825:
			medida = "Megabytes"
			valor = (valor/1024)/1024
		elif valor < 1099511627777:
			medida = "Gigabytes"
			valor = ((valor/1024)/1024)/1024
		else:
			medida = "Terabytes"
			valor = (((valor/1024)/1024)/1024)/1024
		return (medida, valor)

	def _percent_str(cpuuse=0, psize=50):
		pstr = '['
		for x in range(1, psize):
			if x <= int((cpuuse*psize)/100):
				pstr = pstr + '#'
			else:
				pstr = pstr + ' '
		pstr = pstr + ']'
		return (pstr)

	def showinfo():	
		print ("  ----------------------------------------------------------------------")
		print ("  PCpractico.es Wmon v0.52b (07/05/2014)                                ")
		print ("  Developer: Francisco Martínez Estellés                                ")
		print ("* ------------ GENERAL SYSTEM INFO -------------------------------------")
		try:
			print ("* Platform: {}".format(platform.platform()))
		except:
			Print ("* Patform: ??")
		wm_system = platform.system()
		print ("* System: {}".format( wm_system ))
		print ("* Release: {}".format(platform.release()))
		print ("* Version: {}".format(platform.version()))

		print ("* CPU ID: {}".format(platform.processor()))
		print ("* CPU Cores: {0}".format( psutil.cpu_count() ))

		print ("* UPTIME: {}".format(  datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%d-%m-%Y %H:%M:%S')  ))

		try:
			cpuuse = psutil.cpu_percent(interval=2)
		except:
			cpuuse = 0

		print ("* CPU Use: {0} {1}%".format( pymon._percent_str(cpuuse, 37), cpuuse ))

		try:
			usocores = psutil.cpu_percent(interval=2, percpu=True)
			for x in range(psutil.cpu_count()):
				print ("     - USO CPU Core {0}: {1} {2}%".format( x+1,  pymon._percent_str(usocores[x],25),   usocores[x]   ))
		except:
			print ("	- No multicore CPU")
		try:
			memuse = psutil.virtual_memory().percent
			memtotal = psutil.virtual_memory().total
		except:
			memuse = 0
			memtotal = 0
		print ("* Mem use: {0} {1}% of {2:,.2f} {3}".format(pymon._percent_str(memuse, 37),  memuse, pymon._omedida(int(memtotal))[1], pymon._omedida(int(memtotal))[0] ))

		print ("* ------------ SYSTEM UNITS -------------------------------------")
		'''try:
			for parts in psutil.disk_partitions():
				if 'fixed' in parts.opts:
					print ("- Unit {0} : {1} {2}% Used of {3:,.2f} {4}".format(parts.device, pymon._percent_str(psutil.disk_usage(parts.mountpoint).percent, 10)  ,psutil.disk_usage(parts.mountpoint).percent, pymon._omedida(psutil.disk_usage(parts.mountpoint).total)[1], pymon._omedida(psutil.disk_usage(parts.mountpoint).total)[0] ))
		except:
			pass  '''
		for parts in psutil.disk_partitions():
			if ('fixed' in parts.opts) and ('Windows' in wm_system):
				print ("- Unit {0} : {1} {2}% Used of {3:,.2f} {4}".format(parts.device, pymon._percent_str(psutil.disk_usage(parts.mountpoint).percent, 10)  ,psutil.disk_usage(parts.mountpoint).percent, pymon._omedida(psutil.disk_usage(parts.mountpoint).total)[1], pymon._omedida(psutil.disk_usage(parts.mountpoint).total)[0] ))	
			elif 'Windows' not in wm_system:
				print ("- Unit {0} : {1} {2}% Used of {3:,.2f} {4} [{5}]".format(parts.device, pymon._percent_str(psutil.disk_usage(parts.mountpoint).percent, 10)  ,psutil.disk_usage(parts.mountpoint).percent, pymon._omedida(psutil.disk_usage(parts.mountpoint).total)[1], pymon._omedida(psutil.disk_usage(parts.mountpoint).total)[0], parts.opts ))
		
		print ("* ------------ NETWORK INTERFACES -------------------------------------")
		for x in psutil.net_io_counters(pernic=True):
			try:
				print ("* Interface: {0} [Snd: {1}Bytes (Err: {2})| Rcv: {3}Bytes (Err: {4})]".format(x, psutil.net_io_counters(pernic=True)[x].bytes_sent, psutil.net_io_counters(pernic=True)[x].errin, psutil.net_io_counters(pernic=True)[x].bytes_recv, psutil.net_io_counters(pernic=True)[x].errout ))						
			except:
				print ("! Can't get Network interfaces.")				

		print ("* ------------ LOGED USERS -------------------------------------")
		try:
			wmusers = psutil.users()
		except:
			print ("! Can't get users")
		for users in wmusers:
			if 'Windows' in wm_system:
				print ("USER:{0} LOGED:{1}".format(users.name, datetime.datetime.fromtimestamp(users.started).strftime('%d-%m-%Y %H:%M:%S')  ))
			else:
				print ("USER:{0} LOGED:{1} TERM:{2}".format(users.name, datetime.datetime.fromtimestamp(users.started).strftime('%d-%m-%Y %H:%M:%S'), users.terminal  ))
		print ("* ------------ PROCESS LIST ---------------------------------")		
		fmt = "%-30s %5s %5s  %5s %s"		
		print (fmt % ( "User", "Pid", "%CPU", "%MEM", "Process" ))
		print (fmt % ( "----------", "---", "----", "----", "----------" ))
		err=0
		try:
			xpids = psutil.pids()
		except:
			err=1
		if err == 0:
			for x in xpids:
				err=0
				try:
					p = psutil.Process(x)
				except:
					err=1
				if err == 0:
					try:
						proc_name = p.name()
					except:
						proc_name = "?"
					try: 
						''' proc_user = p.username().split('\\')[1]  '''
						proc_user = p.username()
					except:
						proc_user = " "
					print (fmt % ( proc_user, p.pid, p.cpu_percent(interval=0.02), round(p.memory_percent(),1), proc_name ))
		print ("* ------------ NETWORK STATUS ---------------------------------")	
		fmt = "%-15s %-5s %-15s %-5s %12s %-6s %s"		
		print (fmt % ( "Local", "LPort", "Remote", "RPort",  "Status", "Pid", "Service"))
		print (fmt % ( "---------------", "-----", "---------------", "-----" , "------------", "-----", "----------" ))
		for conn in psutil.net_connections():		
			cproc = ""
			try:
				craddr = conn.raddr[0]
				crport = conn.raddr[1]
			except:
				craddr = " "
				crport = " "
			try:
				if conn.pid:
					cproc = psutil.Process(conn.pid).name()
			except:
				pass
			print (fmt % (conn.laddr[0], conn.laddr[1], craddr, crport, conn.status, conn.pid, cproc ))

						
pymon.showinfo()