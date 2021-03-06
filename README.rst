================================
Wmon - Python System info Script
================================


Overview
********



  This simple Script is a first try to develop a simple agent to monitoring computers from remote server.

Processes
*********

  For now, this script can return a plain text report with this:


  - Basic system info.
  - CPU and RAM Load.
  - Hard Disk status.
  - Logged users.
  - Network Status
  - System services and running programs.
  - Listening ports and established connections.

New Features in this version:
*****************************
  - Add Compatibility with Python 2


Install:
********
  
  You can install wmon from Pypi:
  ::

	pip install wmon

  May will need to specify the version of Pypi:
  ::

  	pip3 install wmon

  Also you can install from console:
  ::

	python setup.py install

  Specific for Python3:
  ::

  	python3 setup.py install

Examples:
*********

  Linux Mint 16 output:

	::
			
		  ----------------------------------------------------------------------
		  PCpractico.es Wmon v0.52b (07/05/2014)                                
		* ------------ GENERAL SYSTEM INFO -------------------------------------
		* Platform: Linux-3.11.0-12-generic-x86_64-with-LinuxMint-16-petra
		* System: Linux
		* Release: 3.11.0-12-generic
		* Version: #19-Ubuntu SMP Wed Oct 9 16:20:46 UTC 2013
		* CPU ID: x86_64
		* CPU Cores: 4
		* UPTIME: 08-05-2014 10:19:48
		* CPU Use: [#                                   ] 3.9%
			 - USO CPU Core 1: [                        ] 1.5%
			 - USO CPU Core 2: [                        ] 2.5%
			 - USO CPU Core 3: [                        ] 3.5%
			 - USO CPU Core 4: [                        ] 1.0%
		* Mem use: [######                              ] 17.7% of 3.66 Gigabytes
		* ------------ SYSTEM UNITS -------------------------------------
		- Unit /dev/sda5 : [####     ] 49.1% Used of 24.32 Gigabytes [rw,errors=remount-ro]
		* ------------ NETWORK INTERFACES -------------------------------------
		* Interface: eth0 [Snd: 0Bytes (Err: 0)| Rcv: 0Bytes (Err: 0)]
		* Interface: wlan0 [Snd: 7194860Bytes (Err: 0)| Rcv: 173826909Bytes (Err: 0)]
		* Interface: lo [Snd: 100860Bytes (Err: 0)| Rcv: 100860Bytes (Err: 0)]
		* ------------ LOGED USERS -------------------------------------
		USER:pcpractico LOGED:08-05-2014 10:19:12 TERM:tty7
		USER:pcpractico LOGED:08-05-2014 11:36:00 TERM:pts/3
		* ------------ PROCESS LIST ---------------------------------
		User                             Pid  %CPU   %MEM Process
		----------                       ---  ----   ---- ----------
		root                               1   0.0    0.1 init
		root                               2   0.0    0.0 kthreadd
		root                               3   0.0    0.0 ksoftirqd/0
		root                               4   0.0    0.0 kworker/0:0
		root                               5   0.0    0.0 kworker/0:0H
		root                               7   0.0    0.0 migration/0
		root                               8   0.0    0.0 rcu_bh
		root                               9   0.0    0.0 rcuob/0
		root                              10   0.0    0.0 rcuob/1
		root                              11   0.0    0.0 rcuob/2
		root                              12   0.0    0.0 rcuob/3
		pcpractico                      1459   0.0    0.1 at-spi-bus-launcher
		pcpractico                      1463   0.0    0.0 dbus-daemon
		pcpractico                      1466   0.0    0.1 at-spi2-registryd
		pcpractico                      1475   0.0    0.5 cinnamon-settings-daemon
		pcpractico                      1844   0.0    0.3 cinnamon-screensaver
		pcpractico                      1847   0.0    0.0 sh

		* ------------ NETWORK STATUS ---------------------------------
		Local           LPort Remote          RPort       Status Pid    Service
		--------------- ----- --------------- ----- ------------ -----  ----------
		0.0.0.0         17500                             LISTEN 1737   CloudStack
		0.0.0.0         445                               LISTEN None   
		0.0.0.0         139                               LISTEN None   
		127.0.1.1       53                                LISTEN None   
		0.0.0.0         22                                LISTEN None   
		127.0.0.1       631                               LISTEN None   
		192.168.1.11    34809 211.22.175.76   80      CLOSE_WAIT 17374  plugin_host
		::              445                               LISTEN None   
		::              139                               LISTEN None   
		::              22                                LISTEN None   
		::1             631                               LISTEN None   



  Windows 8 Output:

	::

		  ----------------------------------------------------------------------
		  PCpractico.es Wmon v0.52b (07/05/2014)                                
		* ------------ GENERAL SYSTEM INFO -------------------------------------
		* Platform: Windows-8-6.2.9200
		* System: Windows
		* Release: 8
		* Version: 6.2.9200
		* CPU ID: Intel64 Family 6 Model 37 Stepping 5, GenuineIntel
		* CPU Cores: 4
		* UPTIME: 10-04-2014 18:47:24
		* CPU Use: [#                                   ] 2.9%
			 - USO CPU Core 1: [                        ] 3.9%
			 - USO CPU Core 2: [                        ] 2.3%
			 - USO CPU Core 3: [                        ] 0.8%
			 - USO CPU Core 4: [                        ] 3.9%
		* Mem use: [##########                          ] 28.8% of 7.99 Gigabytes
		* ------------ SYSTEM UNITS -------------------------------------
		- Unit C:\ : [#######  ] 75.1% Used of 223.23 Gigabytes
		- Unit D:\ : [###      ] 36.6% Used of 100.00 Megabytes
		- Unit F:\ : [#########] 99.4% Used of 465.54 Gigabytes
		* ------------ NETWORK INTERFACES -------------------------------------
		* Hostname: pcpractico
		* IP Address: 192.168.1.9
				 Snd          Rcv Err-out  Err-in  Interface
		------------ ------------ ------- -------  ----------
			973.62Kb       0.00B        0       0  VMware Network Adapter VMnet1
			 73.20Mb       3.29Gb       0       0  Ethernet
			974.08Kb     613.80Kb       0       0  VMware Network Adapter VMnet8
			  0.00B        0.00B        0       0  Loopback Pseudo-Interface 1
		* ------------ LOGED USERS -------------------------------------
		USER:PCpractico LOGED:08-05-2014 08:33:14
		* ------------ PROCESS LIST ---------------------------------
		User                             Pid  %CPU   %MEM Process
		----------                       ---  ----   ---- ----------
		NT AUTHORITY\SYSTEM                0 240.0    0.0 System Idle Process
		NT AUTHORITY\SYSTEM                4   0.0    0.0 System
										 300   0.0    0.0 ?
										6896   0.0    0.1 ?
										7436   0.0    0.1 ?
		pcpractico\pcp                  7604   0.0    0.9 explorer.exe
		pcpractico\pcp                 11428   0.0    0.1 splwow64.exe
		pcpractico\pcp                  6280   0.0    0.1 nvtray.exe
		pcpractico\pcp                 10712   0.0    0.1 aetcrss1.exe
										8112   0.0    0.1 ?
		* ------------ NETWORK STATUS ---------------------------------
		Local           LPort Remote          RPort       Status Pid    Service
		--------------- ----- --------------- ----- ------------ -----  ----------
		0.0.0.0         111                               LISTEN 2784   
		0.0.0.0         135                               LISTEN 820    
		192.168.1.9     139                               LISTEN 4      System
		192.168.175.1   139                               LISTEN 4      System
		192.168.240.1   139                               LISTEN 4      System
		0.0.0.0         443                               LISTEN 3132   
		0.0.0.0         554                               LISTEN 3812   
		0.0.0.0         902                               LISTEN 2992   
		192.168.1.9     26430 192.168.1.254   445    ESTABLISHED 4      System
		192.168.1.9     26435 157.55.236.85   443    ESTABLISHED 7604   explorer.exe
		192.168.1.9     26512 173.194.66.125  5222   ESTABLISHED 8724   chrome.exe
		0.0.0.0         49154                             LISTEN 932    
		0.0.0.0         49155                             LISTEN 600    
		127.0.0.1       49156 127.0.0.1       5354   ESTABLISHED 1896