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
    while(True): #port 16 mogelijk fout gevoelig
        ser.write("#0P1722#8P1500#13P1722#16P1277#24P1500#29P1722#1P1922#9P1722#14P1922#17P1277#25P1077#30P1277T200\r".encode())
        sleep(time)
        ser.write("#0P1922#8P1500#13P1522#16P1477#24P1500#29P1522#1P1922#9P1722#14P1922#17P1277#25P1077#30P1277T200\r".encode())
        sleep(time)
        ser.write("#0P1922#8P1500#13P1522#16P1477#24P1500#29P1522#1P1722#9P1722#14P1722#17P1277#25P1277#30P1277T200\r".encode())
        sleep(time)
        ser.write("#0P1922#8P1500#13P1522#16P1477#24P1500#29P1522#1P1722#9P1922#14P1722#17P1077#25P1277#30P1077T200\r".encode())
        sleep(time)
        ser.write("#0P1722#8P1500#13P1722#16P1277#24P1500#29P1722#1P1722#9P1922#14P1722#17P1077#25P1277#30P1077T200\r".encode())
        sleep(time)
        ser.write("#0P1722#8P1500#13P1722#16P1277#24P1500#29P1722#1P1722#9P1722#14P1722#17P1277#25P1277#30P1277T200\r".encode())
        sleep(time)
                
ser.close()
