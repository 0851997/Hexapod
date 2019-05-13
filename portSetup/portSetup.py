import Adafruit_BBIO.UART as UART
import serial

class Ports:
    #variables seconds, port name, port, baubrate
    def __init__(self, uart, portl, rate, name):
        UART.setup(uart)
        self.ser = serial.Serial(port = portl, baudrate=rate)
        self.name = name
        self.ser.close()
        self.ser.open()

    def getPort(self):
        return self.ser