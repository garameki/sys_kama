# raspi_system_temperature
Measure 2 temps, Show 2 temps and using raspberry Pi 3 B+

To make sys_kama.py work as daemon(service):

	1. Put sys_kama.service into /etc/systemd/system/
	2. systemctl enable sys_kama
	3. sudo reboot

	Warning:
		1. recognize path to sys_kama.sh
		2. chmod 750 sys_kama.sh
	How to recognize addition to service:
		systemctl list-unit-files --type=service | grep sys_kama

