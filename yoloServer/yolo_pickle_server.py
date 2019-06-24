import socket
import threading
import pickle
import time

class Server:
    def __init__(self, ipAddr=socket.gethostbyname(socket.gethostname()), port=10000, ready=None):
        self.HOST = ipAddr
        self.PORT = port
        self.rectCenterWidth = 300
        self.dimensionRectangleWidth = 0
        self.ready = ready
        self.s = None

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()
        self.conn, self.addr = self.s.accept()
        self.ready.set()

    def run(self):
        while True:
            data = self.conn.recv(4096)
            if(data!=b''):
                self.data_arr = pickle.loads(data)
                self.rectCenterWidth, self.dimensionRectangleWidth = self.data_arr
                self.conn.send(data)
