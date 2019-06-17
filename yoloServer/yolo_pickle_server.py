import socket
import threading
import pickle

class Server:
    def __init__(self, ipAddr, port, ready=None):
        self.HOST = ipAddr
        self.PORT = port
        self.ready = ready
        self.s = None

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        self.ready.set()

    def run(self):
        print ('Connected by', self.addr)
        while True:
            self.data = self.conn.recv(4096)
            if(data!=b''):
                self.data_arr = pickle.loads(self.data)
                dimensionRectangle,rectCenter,distanceCenterToBorder= self.data_arr
                print(self.data_arr)

                self.dimensionRectangleWidth, self.dimensionRectangleHeight=dimensionRectangle
                self.rectCenterWidth, self.rectCenterHeight=rectCenter
                self.distancBorderWidth,self.distanceBorderHeight=distanceCenterToBorder
                print(dimensionRectangle,rectCenter,distanceCenterToBorder)
                values = self.dimensionRectangleWidth, self.dimensionRectangleHeight, self.rectCenterWidth, self.rectCenterHeight, self.distancBorderWidth, self.distanceBorderHeight
                print(values)
                self.conn.send(self.data)
