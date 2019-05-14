import Adafruit_BBIO.UART as UART
import serial
from time import sleep

#object ports
port = None
def ports(port1):
    global port
    port = port1

def stableStance():
    UART.setup(port.uart)
    ser = serial.Serial(port = port.port, baudrate=port.baudrate)
    ser.close()
    ser.open()
    if ser.isOpen():
        #stable stance
        ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
        sleep(0.5)
    ser.close()

def sit():
    UART.setup(port.uart)
    ser = serial.Serial(port = port.port, baudrate=port.baudrate)
    ser.close()
    ser.open()
    if ser.isOpen():
        ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
        sleep(0.5)
        #B V=14,1,25  H=13,0,24 Right Front Leg, Right Rear Leg, Left Center Leg
        #A V=30,17,9  H=29,16,8 Left Front Leg, Left Rear Leg, Right Center Leg
        ser.write("#30P1139#9P1861#17P1139#14P1861#1P1861#25P1139T500\r".encode())
        sleep(0.5)
        ser.write("#14P2056#1P2056#25P944#30P944#9P2056#17P944T500\r".encode())
        sleep(0.5)
        ser.write("#14P2350#1P2350#25P650#30P650#9P2350#17P650 #31P650#26P650#18P650#2P2350#10P2350#15P2350T500\r".encode())
        sleep(0.5)
    ser.close()
