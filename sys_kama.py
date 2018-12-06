import math
import sys
sys.path.append("/home/pi/src/sys_kama")
from ht16k33 import Ht16k33
from max31856 import Max31856
from acm1602 import Acm1602
import time
import threading
	
def disp_fault_to_acm1602():
	pass

def mes_pri(spi,ht):
	temps = spi.read()
	print(temps)
	if temps["FAULT"] ==0:
		sTemp =str(math.floor(temps["HJ"]*0.0625))
	else:
		spi.analyze_fault()
		disp_fault_to_acm1602()
		sTemp = "F-"+("0"+str(temps["FAULT"]))[-2:]
	ht.print(sTemp,2)
	time.sleep(1)


DEVICE_BUS = 1
DEVICE_ADDR0 = 0x70
DEVICE_ADDR1 = 0x71

ht0 = Ht16k33(DEVICE_BUS,DEVICE_ADDR0)
ht1 = Ht16k33(DEVICE_BUS,DEVICE_ADDR1)

SPI = 0
CE0 = 0
CE1 = 1
spi0 = Max31856(SPI,CE0)
spi1 = Max31856(SPI,CE1)


while True:
	mes_pri(spi0,ht0)
	mes_pri(spi1,ht1)
	time.sleep(1)
