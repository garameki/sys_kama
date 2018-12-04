import math
import sys
sys.path.append("/home/pi/src/sys_kama")
from ht16k33 import Ht16k33
from max31856 import Max31856


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

temps0 = spi0.read()
temps1 = spi1.read()

temp0 =math.floor(temps0["HJ"]*0.0625)
temp1 =math.floor(temps1["HJ"]*0.0625)
if temp0 < -1000:
	sTemp0 = "FAUL"
else:
	sTemp0 = str(temp0)
if temp1 < -1000:
	sTemp1 = "FAUL"
else:
	sTemp1 = str(temp1)

ht0.print(sTemp0,2)
ht1.print(sTemp1,2)



