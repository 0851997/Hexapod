import Adafruit_BBIO.UART as UART
import serial
from time import sleep

time = 0.2
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    #stable stance
    ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
    sleep(0.5)
    while(True):            #Tripod Gait A is described                        Tripod Gait B is described
        ser.write("#29P1722#16P1277#8P1500 #30P1277#17P1277#9P1722 #10P1944 #0P1722#13P1722#24P1500 #1P1922#14P1922#25P1077 #26P1055 T200\r".encode())
        sleep(time)
        ser.write("#29P1522#16P1477#8P1500 #30P1277#17P1277#9P1722 #10P1744 #0P1922#13P1522#24P1500 #1P1922#14P1922#25P1077 #26P855  T200\r".encode())
        sleep(time)
        ser.write("#29P1522#16P1477#8P1500 #30P1277#17P1277#9P1722 #10P1744 #0P1922#13P1522#24P1500 #1P1722#14P1722#25P1277 #26P855  T200\r".encode())
        sleep(time)
        ser.write("#29P1522#16P1477#8P1500 #30P1077#17P1077#9P1922 #10P1744 #0P1922#13P1522#24P1500 #1P1722#14P1722#25P1277 #26P855  T200\r".encode())
        sleep(time)
        ser.write("#29P1722#16P1277#8P1500 #30P1077#17P1077#9P1922 #10P1944 #0P1722#13P1722#24P1500 #1P1722#14P1722#25P1277 #26P1055 T200\r".encode())
        sleep(time)
        ser.write("#29P1722#16P1277#8P1500 #30P1277#17P1277#9P1722 #10P1944 #0P1722#13P1722#24P1500 #1P1722#14P1722#25P1277 #26P1055 T200\r".encode())
        sleep(time)
                
ser.close()
