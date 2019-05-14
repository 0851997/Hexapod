class Ports:
    #variables seconds, port name, port, baubrate
    def __init__(self, uart, portl, rate):
        self.uart = uart
        self.port = portl
        self.baudrate = rate
