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
    ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
    sleep(0.5)
    while(True):            #Tripod Gait A is described                        Tripod Gait B is described
        ser.write("#29P1722#16P1278#8P1500 #30P1177#17P1177#9P1622 #10P1944 #0P1722#13P1722#24P1500 #1P2022#14P2022#25P1177 #26P1055 T50\r".encode())
        sleep(time)
        ser.write("#29P1522#16P1478#8P1500 #30P1177#17P1177#9P1622 #10P2144 #0P1922#13P1522#24P1500 #1P2022#14P2022#25P1177 #26P1255  T50\r".encode())
        sleep(time)
        ser.write("#29P1522#16P1478#8P1500 #30P1177#17P1177#9P1622 #10P2144 #0P1922#13P1522#24P1500 #1P1822#14P1822#25P1377 #26P1255  T50\r".encode())
        sleep(time)
        ser.write("#29P1522#16P1478#8P1500 #30P977#17P977#9P1622 #10P2144 #0P1922#13P1522#24P1500 #1P1822#14P1822#25P1377 #26P1255  T50\r".encode())
        sleep(time)
        ser.write("#29P1722#16P1278#8P1500 #30P977#17P977#9P1822 #10P1944 #0P1722#13P1722#24P1500 #1P1822#14P1822#25P1377 #26P1055 T50\r".encode())
        sleep(time)
        ser.write("#29P1722#16P1278#8P1500 #30P1177#17P1177#9P1822 #10P1944 #0P1722#13P1722#24P1500 #1P1822#14P1822#25P1377 #26P1055 T50\r".encode())
        sleep(time)
                
ser.close()
