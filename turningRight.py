import Adafruit_BBIO.UART as UART
import serial
from time import sleep

UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    #stand
    ser.write("#31P1166#26P1166#18P1166#30P1333#25P1333#17P1333#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1666#9P1666#14P1666#15P1833#10P1833#2P1833T200\r".encode())
    sleep(0.2)
    while(True):
        #B V=14,1,25  H=13,0,24 Right Front Leg, Right Rear Leg, Left Center Leg
        #A V=30,17,9  H=29,16,8 Left Front Leg, Left Rear Leg, Right Center Leg
        #lynx 0
        ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
        sleep(0.1)
        #lynx 1
        ser.write("#29P1922#8P1700#16P1478#14P1861#1P1861#25P1139#13P1078#0P1522#24P1300T50\r".encode())
        sleep(0.1)
        #lynx 2
        ser.write("#14P1666#1P1666#25P1333T50\r".encode())
        sleep(0.1)
        #lynx 3
        ser.write("#30P1139#9P1861#17P1139T50\r".encode())
        sleep(0.1)
        #lynx 4
        ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
        sleep(0.1)
        #lynx 5
        ser.write("#30P1139#9P1861#17P1139#29P1522#8P1300#16P1078#13P1478#0P1922#24P1700T50\r".encode())
        sleep(0.1)
        #lynx 6
        ser.write("#30P1333#9P1666#17P1333T50\r".encode())
        sleep(0.1)
        #lynx 7
        ser.write("#14P1861#1P1861#25P1139T50\r".encode())
        sleep(0.1)

ser.close()
