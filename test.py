import Adafruit_BBIO.UART as UART
import serial
from time import sleep

UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    while(True):
        print ("Serial is open!")
        ser.write("#0 P2000\r".encode())
        sleep(1)
        ser.write("#8 P1250\r".encode())
        sleep(1)
        ser.write("#13 P2000\r".encode())
        sleep(1)
        ser.write("#16 P2000\r".encode())
        sleep(1)
        ser.write("#24 P1250\r".encode())
        sleep(1)
        ser.write("#29 P2000\r".encode())
        sleep(1)
ser.close()
