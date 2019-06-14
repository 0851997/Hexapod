import socket
import pickle

HOST = '192.168.43.189'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while True:
    data = conn.recv(4096)
    if(data!=b''):
        data_arr = pickle.loads(data)
        dimensionRectangle,rectCenter,distanceCenterToBorder=data_arr
        print(data_arr)

        dimensionRectangleWidth,dimensionRectangleHeight=dimensionRectangle
        rectCenterWidth,rectCenterHeight=rectCenter
        distancBorderWidth,distanceBorderHeight=distanceCenterToBorder
        print(dimensionRectangle,rectCenter,distanceCenterToBorder)
        values = dimensionRectangleWidth,dimensionRectangleHeight,rectCenterWidth,rectCenterHeight,distancBorderWidth,distanceBorderHeight
        print(values)
        conn.send(data)
