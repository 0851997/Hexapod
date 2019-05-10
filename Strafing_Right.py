import Adafruit_BBIO.UART as UART
import serial
from time import sleep

#variables seconds, port name, port, baubrate
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    #stable stance
    ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
    sleep(0.5)
    while(True):
        #B Vertical Ports=14,1,25  Horizontal Ports=13,0,24  Corresponding legs: Right Front Leg, Right Rear Leg, Left Center Leg
        #A Vertical Ports=30,17,9  Horizontal Ports=29,16,8  Corresponding legs: Left Front Leg, Left Rear Leg, Right Center Leg
        #lynxmotion guide 0 in README
        ser.write("#31P1255#30P1277#26P1055#25P1477#18P1255#17P1277 #14P1722#15P2144#9P1722#10P1744#1P1722#2P2144 T100\r".encode())
        sleep(0.05)
        #lynxmotion guide 1 in README
        ser.write("#31P855#30P1277#18P855#17P1277 #9P1522#10P1944 T100\r".encode())
        sleep(0.05)
        #lynxmotion guide 2 in README
        ser.write("#31P1055#30P1477#26P1255#25P1277#18P1055#17P1477 #14P1522#15P744#9P1722#10P2144#1P1522#2P744 T100\r".encode())
        sleep(0.05)
        #lynxmotion guide 3 in README
        ser.write("#26P855#25P1277 #14P1522#15P1744#1P1522#2P1744 T100\r".encode())
        sleep(0.05)
        #lynxmotion guide 4 in README
        ser.write("#31P1255#30P1277#26P1055#25P1477#18P1255#17P1277 #14P1722#15P2144#9P1722#10P1744#1P1722#2P2144 T100\r".encode())
        sleep(0.05)
ser.close()

def reverse():
    print("q")

def turnRight():
    print("r")

def turnLeft():
    print("k")

def sideRight():
    print("s")

def sideLeft():
    print("v")

