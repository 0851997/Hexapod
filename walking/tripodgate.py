import Adafruit_BBIO.UART as UART
import serial
from time import sleep

def tripodWalking(time, uart, portl, rate):
    UART.setup(uart)
    ser = serial.Serial(port = portl, baudrate=rate)
    ser.close()
    ser.open()
    if ser.isOpen():
        ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
        sleep(0.5)
        while(True):
            #B Vertical=14,1,25  Horizontal=13,0,24 Right Front Leg, Right Rear Leg, Left Center Leg
            #A Vertical=30,17,9  Horizontal=29,16,8 Left Front Leg, Left Rear Leg, Right Center Leg
            #see lynxmotion ssc-32U servo controller board guide page 28
            #lynx 0
            ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
            sleep(0.05)
            #lynx 1
            ser.write("#29P1922#8P1300#16P1478#14P1861#1P1861#25P1139#13P1478#0P1922#24P1300T50\r".encode())
            sleep(0.05)
            #lynx 2
            ser.write("#14P1722#1P1722#25P1277T50\r".encode())
            sleep(time)
            #lynx 3
            ser.write("#30P1139#9P1861#17P1139T50\r".encode())
            sleep(0.05)
            #lynx 4
            ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
            sleep(0.05)
            #lynx 5
            ser.write("#30P1139#9P1861#17P1139#29P1522#8P1700#16P1078#13P1078#0P1522#24P1700T50\r".encode())
            sleep(0.05)
            #lynx 6
            ser.write("#30P1277#9P1722#17P1277T50\r".encode())
            sleep(time)
            #lynx 7
            ser.write("#14P1861#1P1861#25P1139T50\r".encode())
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

