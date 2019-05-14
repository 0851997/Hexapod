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
        #
        # A up B idle
        ser.write("#26P1255#25P1277 #14P1722#15P1744#1P1722#2P1744 T500\r".encode())
        sleep(0.5)
        # A duw B intrekken
        ser.write("#31P1055#30P1477#18P1055#17P1477 #9P1722#10P2144 T500\r".encode())
        sleep(0.5)
        # A down B idle
        ser.write("#26P855#25P1477 #14P1522#15P1944#1P1522#2P1944 T500\r".encode())
        sleep(0.5)
        # A idle B omhoog
        ser.write("#31P1255#30P1277#18P1255#17P1277 #9P1722#10P1744 T500\r".encode())
        sleep(0.5)
        # A duw B gaat benen ver zetten
        ser.write("#26P1055#25P1477 #14P1522#15P2144#1P1522#2P2144 T500\r".encode())
        sleep(0.5)

        ser.write("#31P855#30P1477#18P855#17P1477 #9P1522#10P2144 T500\r".encode())
        sleep(0.5)
        # A idle B intrekken
        # A idle B down
        '''
        #State 0: gait B gaat omhoog en gait A duwt
        ser.write("#31P1255#30P1277#26P1055#25P1477#18P1255#17P1277 #14P12#15P2144#9P1722#10P1744#1P1722#2P2144 T500\r".encode())
        sleep(0.5)
        #State 1: gait B gaat intrekken en gait A doet niks
        ser.write("#31P855#30P1277#18P855#17P1277 #9P1522#10P1944 T500\r".encode())
        sleep(0.5)
        
        #State 2: gait B gaat duwen en gait A omhoog
        ser.write("#31P1055#30P1677#26P1255#25P1177#18P1055#17P1677 #14P1922#15P1744#9P2122#10P2144#1P1922#2P1744 T500\r".encode())
        sleep(0.5)
       
        #Sate 3: gait B doet niks en gait A gaat benen ver zetten
        ser.write("#26P855#25P1277 #14P1522#15P1944#1P1522#2P1944 T500\r".encode())
        sleep(0.5)
        
        #State 4: gait B omhoog en gait A gaat intrekken
        ser.write("#31P1255#30P1277#26P1055#25P1477#18P1255#17P1277 #14P1722#15P2144#9P1722#10P1744#1P1722#2P2144 T500\r".encode())
        sleep(0.5)'''
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

