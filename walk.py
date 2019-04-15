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
    i = 0
    while(True):
        #lynx 0
        ser.write("#29P1722#8P1500#16P1278#14P2056#1P2056#25P944#13P1278#0P1722#24P1500T50\r".encode())
        sleep(0.5)
        #lynx 1
        ser.write("#29P1522#8P1700#16P1078#14P1861#1P1861#25P1139#131578#0P1922#24P1300T50\r".encode())
        sleep(0.5)
        #lynx 2
        ser.write("#14P1666#1P1666#25P1333T50\r".encode())
        sleep(0.5)
        #lynx 3
        ser.write("#30P1139#9P1861#17P1139T50\r".encode())
        sleep(0.5)
        #lynx 4
        ser.write("#30P944#9P2056#17P944#29P1722#8P1500#16P1278#13P1278#0P1722#24P1500T50\r".encode())
        sleep(0.5)
        #lynx 5
        ser.write("#30P1139#9P1861#17P1139#29P1922#8P1300#16P1478#13P1078#0P1522#24P1700T50\r".encode())
        sleep(0.5)
        #lynx 6
        ser.write("#30P1333#9P1666#17P1333T50\r".encode())
        sleep(0.5)
        #lynx 7
        ser.write("#14P1861#1P1861#25P1139T50\r".encode())
        sleep(0.5)
        #B V=14,1,25  H=13,0,24
        #A V=30,9,17  H=29,8,16
        '''#up one side A port 0,13,24 gate B
        ser.write("#25P944#24P1300#14P2056#1P2056#13P1578#0P1922T100\r".encode())
        sleep(0.5)
        #down one side A
        ser.write("#25P1333#24P1300#13P1578#0P1922#1P1666#14P1666T100\r".encode())
        sleep(0.5)
        #forward A
        ser.write("#29P1922#24P1500#16P1478#0P1722#8P1300#13P1278T100\r".encode())
        sleep(0.5)
        #up other side A port 8,16,29 gate A
        ser.write("#30P944#17P944#29P1422#16P1078#9P2056#8P1800T100\r".encode())
        sleep(0.5)
        #down other side A
        ser.write("#30P1333#17P1333#29P1422#16P1078#8P1800#9P1666T100\r".encode())
        sleep(0.5)
        #forward A
        ser.write("#29P1722#24P1700#16P1278#13P1078#8P1500#0P1522T100\r".encode())
        sleep(0.5)'''
        #i=i+1
        if i == 3:
            ser.write("#31P1166#26P1166#18P1166#30P1333#25P1333#17P1333#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1666#9P1666#14P1666#15P1833#10P1833#2P1833T200\r".encode())
            sleep(0.2)
            i=0
        #up one side port 0,13,24
        #ser.write("#25P944#26P1056#24P1222#14P2056#1P2200#15P1944#2P1944#13P1355#0P2000#31P1166#18P1166#30P1333#17P1333#29P1722#16P1350#8P1300#9P1666#10P1833T1000\r".encode())
        #sleep(1)
        #ser.write("#26P1166#25P1333#24P1222#13P1355#0P2000#1P1666#14P1666#15P1833#2P1833#31P1166#18P1166#30P1333#17P1333#29P1722#16P1350#8P1300#9P1666#10P1833T1000\r".encode())
        #sleep(1)
        #up other side port 8,16,29
        #ser.write("#30P944#17P600#18P1056#31P1056#29P1544#16P1200#9P2056#10P1944#8P1600#26P1166#25P1333#24P1500#13P1278#0P1500#1P1666#14P1666#15P1833#2P1833T1000\r".encode())
        #sleep(1)
        #ser.write("#31P1166#18P1166#30P1333#17P1333#29P1544#16P1200#8P1600#9P1666#10P1833#26P1166#25P1333#24P1500#13P1278#0P1500#1P1666#14P1666#15P1833#2P1833T1000\r".encode())
        #sleep(1)
        #stand
        #ser.write("#31P1166#26P1166#18P1166#30P1333#25P1333#17P1333#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1666#9P1666#14P1666#15P1833#10P1833#2P1833T1500\r".encode())
        #sleep(1.5)
ser.close()
