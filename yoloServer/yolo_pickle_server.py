import socket
import threading
import pickle

data_arr = None
rectCenterWidth = 300
conn = None

class Server(threading.Thread):
    def begin(self, ipAddr, port, listeners=1):
        self.HOST = ipAddr
        self.PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(listeners)
        global conn
        conn, self.addr = self.s.accept()

    def run(self):
        print ('Connected by', self.addr)
        while True:
            data = self.conn.recv(4096)
            if(data!=b''):
                global data_arr
                data_arr = pickle.loads(data)
                dimensionRectangle,rectCenter,distanceCenterToBorder=data_arr
                print(data_arr)

                global rectCenterWidth
                dimensionRectangleWidth,dimensionRectangleHeight=dimensionRectangle
                rectCenterWidth,rectCenterHeight=rectCenter
                distancBorderWidth,distanceBorderHeight=distanceCenterToBorder
                print(dimensionRectangle,rectCenter,distanceCenterToBorder)
                values = dimensionRectangleWidth,dimensionRectangleHeight,rectCenterWidth,rectCenterHeight,distancBorderWidth,distanceBorderHeight
                print(values)
                self.conn.send(data)
