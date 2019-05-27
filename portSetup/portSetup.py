import Adafruit_BBIO.UART as UART
import serial

class Configurations:
    def __init__(self, uartPort, port, baudrate):
        self.uartPort = uartPort
        self.port = port
        self.baudrate = baudrate

    def initializePorts(self):
        UART.setup(self.uartPort)
        self.serialConn = serial.Serial(port = self.port, baudrate = self.baudrate)