import Adafruit_BBIO.UART as UART
import serial

class Ports():
    def __init__(self):
        self.ser = ''

    #variables seconds, port name, port, baubrate
    def setPort(self, uart, portl, rate):
        UART.setup(uart)
        self.ser = serial.Serial(port = portl, baudrate=rate)

    def getPort(self):
        return self.ser