import pyupm_i2clcd as lcd
import socket
import fcntl
import struct
import time
from wireless import Wireless 

def getIP(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
        )[20:24])

myLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLCD.setColor(0, 255, 0)

myLCD.setCursor(0, 0)

ip = getIP('wlan0')
    
wireless = Wireless()

ssid = wireless.current()

myLCD.write(ssid)

myLCD.setCursor(1,0)

myLCD.write(ip)

while True:
    if ip != getIP('wlan0'):
        myLCD.clear()
        myLCD.setCursor(0,0)
        ssid = wireless.current()
        myLCD.write(ssid)
        ip = getIP('wlan0')
        myLCD.setCursor(1, 0)
        myLCD.write(ip)
    time.sleep(1)
