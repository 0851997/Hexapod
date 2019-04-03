import Adafruit_BBIO.UART as UART
import serial
from time import sleep

def tripodWalking(forward, time, uart, portl, rate):
    UART.setup(uart)
    ser = serial.Serial(port = portl, baudrate=rate)
    ser.close()
    ser.open()
    if ser.isOpen():
        slp=time/1000
        stand="#31P1166#26P1166#18P1166#30P1333#25P1333#17P1333#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1666#9P1666#14P1666#15P1833#10P1833#2P1833T{}\r".format(time)
        ser.write(stand.encode())
        sleep(slp)
        i = 0
        if forward == True:
            while(True):
                #up one side A port 0,13,24 gate 1
                upRight="#25P944#26P1056#24P1300#14P2056#1P2056#15P1944#2P1944#13P1578#0P1922{}\r".format(time)
                ser.write(upRight.encode())
                sleep(slp)
                #down one side A
                downRight="#26P1166#25P1333#24P1300#13P1578#0P1922#1P1666#14P1666#15P1833#2P1833{}\r".format(time)
                ser.write(downRight.encode())
                sleep(slp)
                #forward A
                moveRight="#29P1922#24P1500#16P1478#0P1722#8P1300#13P1278{}\r".format(time)
                ser.write(moveRight.encode())
                sleep(slp)
                #up other side A port 8,16,29 gate 2
                upLeft="#30P944#17P944#18P1056#31P1056#29P1422#16P1078#9P2056#10P1944#8P1800{}\r".format(time)
                ser.write(upLeft.encode())
                sleep(slp)
                #down other side A
                downLeft="#31P1166#18P1166#30P1333#17P1333#29P1422#16P1078#8P1800#9P1666#10P1833{}\r".format(time)
                ser.write(downLeft.encode())
                sleep(slp)
                #forward A
                moveLeft="#29P1722#24P1700#16P1278#13P1078#8P1500#0P1522T{}\r".format(time)
                ser.write(moveLeft.encode())
                sleep(slp)
                i=i+1
                if i == 3:
                    ser.write(stand.encode())
                    sleep(slp)
                    i=0
        elif forward == False:
            print("d")
        else:
            print("k")
    ser.close()


def stopping():
    print("r")


def send():
    print("d")


def setup():
    print("l")


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
