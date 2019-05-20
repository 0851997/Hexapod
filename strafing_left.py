import Adafruit_BBIO.UART as UART
import serial
from time import sleep

time = 0.05
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    #stable stance
    ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T500\r".encode())
    sleep(0.5)
    while(True):
        ser.write("#30P1477#25P1477#17P1477 #14P1522#9P1522#1P1522 T50\r".encode())             #Higher standing stance
        sleep(time)
        ser.write("#25P1177 #9P1822 T50\r".encode())                                            #Center legs position high
        sleep(time)
        ser.write("#26P1255 #10P2144 T50\r".encode())                                           #Center legs position high leftside
        sleep(time)
        ser.write("#25P1477 #9P1522 T50\r".encode())                                            #Center legs position low leftside
        sleep(time)
        ser.write("#14P1822 #1P1822 T50\r".encode())                                            #Rightfront and rightrear legs position high (left side is pulling)
        sleep(time)
        ser.write("#29P1522 #26P1055 #16P1478 #13P1478 #10P1944 #0P1522 T50\r".encode())        #Movement state left to right
        sleep(time)
        ser.write("#14P1522 #1P1522 T50\r".encode())                                            #Rightfront and rightrear legs position low
        sleep(time)
        ser.write("#25P1177 #9P1822 T50\r".encode())                                            #Center legs high possition
        sleep(time)
        ser.write("#26P1255 #10P2144 T50\r".encode())                                           #Center legs position high leftside 
        sleep(time)
        ser.write("#25P1477 #9P1522 T50\r".encode())                                            #Center legs position low leftside
        sleep(time)
        ser.write("#30P1177 #17P1177 T50\r".encode())                                           #Leftfront and leftrear legs position high
        sleep(time)
        ser.write("#29P1722 #26P1055 #16P1278 #13P1278 #10P1944 #0P1722 T50\r".encode())        #Movement state2 left to right (right side is pushing)
        sleep(time)
ser.close()
