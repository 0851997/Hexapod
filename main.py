import portSetup.portSetup as port
import walking.tripodgait as walking
import standing.stableStance as standing
import yoloServer.yolo_pickle_server as server
from time import sleep
import string
import threading

#turnLeftBoudaries = 0 - 85
#strafeLeftBoundary = 85 - 224
#forwardBackwardBoundary = 224 - 416
#strafeRightBoundary = 416 - 555
#turnRightBoundary = 555 - 640
boundary = (85, 224, 416, 555, 640)
centerLocationPoint = 0;
personYLocationBorder = 0;

config = port.Configurations("UART1","/dev/ttyO1",9600)
config.initializePorts()
config.serialConn.close()
config.serialConn.open()

ready = threading.Event()
connection = server.Server('192.168.43.189',10000,ready)
mythread = threading.Thread(target=connection.connect)
mythread.start()
ready.wait()
thread = threading.Thread(target=connection.start)
thread.start()

try:
    if config.serialConn.isOpen():
        standing.stableStance(config)
        # while(True):
        #     mode = input("Press a key for movement command: ")
        #     print(server.data_arr)
        #     for i in range(3):
        #         if mode == 'q':
        #             walking.strafeLeft(config, 0.05)
        #         elif mode == 'w':
        #             walking.tripodWalking(config, 0.05)
        #         elif mode == 'e':
        #             walking.strafeRight(config, 0.05)
        #         elif mode == 'a':
        #             walking.turnLeft(config)
        #         elif mode == 's':
        #             walking.reverse(config, 0.05)
        #         elif mode == 'd':
        #             walking.turnRight(config)
        #         elif mode == 'z':
        #             standing.stableStance(config)
        #             break
        #         elif mode == 'x':
        #             standing.sit(config)
        #             break
                    
        #THIS IS THE INTERFACE FOR THE END OF THE PROJECT
        while(True):
            print(server.data_arr)
            if server.rectCenterWidth < boundary[0]:
                walking.turnLeft()
            elif server.rectCenterWidth < boundary[1]:
                walking.strafeLeft()
            elif server.rectCenterWidth < boundary[2]:
                print ("random")#if personYLocationBorder 
            elif server.rectCenterWidth < boundary[3]:
                walking.strafeRight()
            elif server.rectCenterWidth < boundary[4]:
                walking.turnRight()

except:
    standing.sit(config)
    config.serialConn.close()
    server.conn.close()