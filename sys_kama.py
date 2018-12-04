import sys
sys.path.append("/home/pi/src/sys_kama")
from ht16k33 import Ht16k33

DEVICE_BUS = 1
DEVICE_ADDR0 = 0x70
DEVICE_ADDR1 = 0x71

h1 = H16k33(DEVICE_BUS,DEVICE_ADDR0)
