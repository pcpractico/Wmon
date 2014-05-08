Wmon - Python System info Script
================================

* **Overview**<br>
  This simple Script is a first try to develop a simple agent to monitoring computers from remote server.

* **Processes**<br>
  For now, this script can return a plain text report with this:

  - Basic system info.
  - CPU and RAM Load.
  - Hard Disk status.
  - Logged users.
  - Network Status
  - System services and running programs.
  - Listening ports and established connections.


* **Output:** <br>

 Linux Mint 16 output

```
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

```

* **Dependences:** <br>
Python version: 3.3.3
PSutil 2.1.1

* **Special Thanks to:** <br>
PSutil team.
