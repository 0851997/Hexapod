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
            print ("Port3: ")
            r = input()
            print ("Degree1 0 to 180: ")
            z = input()
            print ("Degree2 0 to 180: ")
            n = input()
            print ("Degree3 0 to 180: ")
            m = input()
            print ("Time in microseconds 65535 is max: ")
            l = int(input())
            z = int(degree(float(z)))
            n = int(degree(float(n)))
            m = int(degree(float(m)))
            if l < 250:
                l=250
            w = "#{}".format(int(s))
            o = "P{}".format(z)
            c = "#{}".format(int(q))
            v = "P{}".format(n)
            u = "#{}".format(int(r))
            h = "P{}".format(m)
            y = "T{}".format(l)
            d = w+o+c+v+u+h+y+str("\r")
            ser.write(d.encode())
            sleep(l/1000)
except KeyboardInterrupt:
    ser.close()