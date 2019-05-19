# raspi_system_temperature
Measure 2 temps, Show 2 temps and using raspberry Pi 3 B+

To make sys_kama.py work as daemon(service):  
  
	1. ln -s /home/pi/src/sys_kama/sys_kama.service /etc/systemd/system/sys_kama.service  
	2. systemctl enable /etc/systemd/system/sys_kama.service  
	3. sudo reboot  
  
	Warning:  
		1. recognize path to sys_kama.sh  
		2. chmod 750 sys_kama.sh  
	How to recognize addition to service:  
		systemctl list-unit-files --type=service | grep sys_kama  
  
置く場所  
========  
	~/src/sys_kama/の中  
  
説明  
====  
 acm1602.py  
 	LCDに表示するためのライブラリ  
 ht16k33.py  
 	4桁8digitのデジタル表示器に数字を出すためのライブラリ  
  
