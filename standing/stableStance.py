import Adafruit_BBIO.UART as UART
import serial
from time import sleep

#object ports
def stableStance(ports):
    UART.setup(ports.uart)
    ser = serial.Serial(port = ports.port, baudrate=ports.baudrate)
    if ser.isOpen():
        #stable stance
        ser.write("#31P1055#26P1055#18P1055#30P1277#25P1277#17P1277#29P1722#24P1500#16P1278#13P1278#8P1500#0P1722#1P1722#9P1722#14P1722#2P1944#10P1944#15P1944T200\r".encode())
        sleep(0.5)
