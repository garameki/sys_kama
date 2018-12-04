#!/usr/bin/env python3

#https://www.javadrive.jp/python/string/index9.html
#数値を文字列に変換(str)


import smbus

import time

class Ht16k33:
	DDD = { }
	DDD["0"] = 0x3F
	DDD["1"] = 0x06
	DDD["2"] = 0x5B
	DDD["3"] = 0x4F
	DDD["4"] = 0x66
	DDD["5"] = 0x6D
	DDD["6"] = 0x7D
	DDD["7"] = 0x27
	DDD["8"] = 0x7F
	DDD["9"] = 0x6F
	DDD["-"] = 0x00

	def __init__(self,dev_bus,dev_addr):
		#(hex) dev_bus
		#(hex) dev_addr
		self.bus = smbus.SMBus(dev_bus)
		self.addr = dev_addr
		self.bus.write_byte(self.addr,0x21)
		self.bus.write_byte(self.addr,0x81)
		self.bus.write_byte(self.addr,0xE0)

	def version(self):
		return "1.1"


		#light strength
	def strength(self,value):
		#(hex) value : 0x0～0xF
		value = int(value)
		if value > 0xF:
			value = 0xF
		elif value < 0x0:
			value = 0x0
		value = value + 0xE0;
		self.bus.write_byte(self.addr,value)

	def print(self,sValue="0000",fColon=False):
		#(String) sValue
		#(boolean) fColon : 0:disappear  1:appear
		sValue = "----" + sValue
		flag = True
		try:
			d4 = Ht16k33.DDD[sValue[-1]]
			d3 = Ht16k33.DDD[sValue[-2]]
			d2 = Ht16k33.DDD[sValue[-3]]
			d1 = Ht16k33.DDD[sValue[-4]]
		except:
			print("sValue contains another of [0-9] letter")
			flag = False
		if flag:
			if fColon == True:
				coron = 0xf
			else:
				coron = 0x0
			data = [d1,0,d2,0,coron,0,d3,0,d4]
			self.bus.write_i2c_block_data(self.addr,0x00,data)

	def close(self):
		print("you don't have to close smbus")

if __name__ == "__main__":

	#SAMPLE
	#	usage:
	#		example1 : $ python3 ht16k33.py 1
	#			if you connect 1 4Dig7Sed-LED
	#		example2 : $ python3 ht16k33.py 2
	#			if you connect 2 4Dig7Sed-LEDs

	from datetime import datetime
	import sys
	
	arg = sys.argv
	if len(arg) == 1:
		print("enter number of 4dig7seg-LED device(s),expect [1-2]")
	else:
		if arg[1] == "1":
			flag1 = True
			flag2 = False
		elif arg[1] == "2":
			flag1 = True
			flag2 = True
		else:
			print("Wrong number,expect [1-2]")
			flag1 = False
			flag2 = False

		if flag1:
			DEVICE_BUS = 1
			DEVICE_ADDR0 = 0x70
			DEVICE_ADDR1 = 0x71

			h1 = Ht16k33(DEVICE_BUS,DEVICE_ADDR0)
			if flag2:h2 = Ht16k33(DEVICE_BUS,DEVICE_ADDR1)

			coron = 0
			count = 1 
			flag = True
			while True:
				try:
					count += 1
					if count == 2:
						ms = datetime.now().strftime("%M%S")
						mult = datetime.now().strftime("%d%H")

						count = 0
					if flag:
						flag = False
						coron = True
					else:
						flag = True
						coron = False
					h1.print(ms,coron)
					if flag2:h2.print(mult,coron)

					time.sleep(0.5)

				except KeyboardInterrupt:
					break

