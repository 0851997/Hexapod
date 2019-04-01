import Adafruit_BBIO.UART as UART
import serial
from time import sleep

UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()

def degree(a):
    b = a/180*2000+500
    return b
try:
    if ser.isOpen():
        while(True):
            print ("Port1: ")
            s = input()
            print ("Port2: ")
            q = input()
            prinf ("Port3: ")
            r = input()
            print ("Degree1 0 to 180: ")
            z = input()
            print ("Degree2 0 to 180: ")
            n = input()
            print ("Degree3 0 to 180: ")
            m = input()
            print ("Time in microseconds 65535 is max: ")
            l = input()
            z = int(degree(float(z)))
            n = int(degree(float(n)))
            m = int(degree(float(m)))
            if l < 250:
                l=250
            ser.write("#",int(s),"P",z,"#",int(q),"P",n,"#",int(r),"P",m,"T",l,"\r".encode())
            sleep(l/1000)
except KeyboardInterrupt:
    ser.close()