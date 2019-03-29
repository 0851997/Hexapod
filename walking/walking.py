import Adafruit_BBIO.UART as UART
import serial
from time import sleep

UART.setup("UART1")

def tripodWalking(forward):
    if forward==True:
        print('a')
    elif forward==False:
        print('d')
    else:
        print('k')
    
def stopping():
    print('r')

def send():
    print('d')

def setup():
    print('l')
 
# ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
# ser.close()
# ser.open()
# if ser.isOpen():
#     while(True):
#         print ("Serial is open!")
#         ser.write("#0 P500\r".encode())
#         sleep(1)
#         ser.write("#0 P2500\r".encode())
#         sleep(1)
# ser.close()
