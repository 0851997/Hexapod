'''import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.43.200', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print(sys.stderr, '\nwaiting to receive message')
    data, address = sock.recvfrom(4096)
 
    print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
    print (sys.stderr, data)

    if data:
        sent = sock.sendto(data, address)
        print(sys.stderr, 'sent %s bytes back to %s' % (sent, address))
'''

import socket
import pickle
from time import sleep

HOST = '192.168.43.189'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
try:
    while True:
        data = conn.recv(4096)
        if(data!=b''):
            data_arr = pickle.loads(data)
            H,B,C=data_arr
            print(data_arr)
            W,L=H
            Z,X=B
            R,V=C
            print(H,B,C)
            print(W,L,Z,X,R,V)
            conn.send(data)
except KeyboardInterrupt:
    conn.close()
