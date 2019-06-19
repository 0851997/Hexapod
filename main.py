import portSetup.portSetup as port
import walking.tripodgait as walking
import standing.stableStance as standing
import yoloServer.yolo_pickle_server as server
import time
import string
import threading

boundary = (85, 224, 416, 555, 640)
centerLocationPoint = 0;
personYLocationBorder = 0;

config = port.Configurations("UART1","/dev/ttyO1",9600)
config.initializePorts()
config.serialConn.close()
config.serialConn.open()

ready = threading.Event()
connection = server.Server('192.168.43.5',9000,ready)
mythread = threading.Thread(target=connection.connect)
mythread.start()
ready.wait()
thread = threading.Thread(target=connection.run)
thread.start()

try:
    if config.serialConn.isOpen():
        standing.stableStance(config)
        timeout = time.time() + 5
        # while(True):
        #     mode = input("Press a key for movement command: ")
        #     print(connection.data_arr)
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
            #turnLeftBoudaries = 0 - 85
            #strafeLeftBoundary = 85 - 224
            #forwardBackwardBoundary = 224 - 416
            #strafeRightBoundary = 416 - 555
            #turnRightBoundary = 555 - 640
            #print(connection.data_arr)
            while (connection.rectCenterWidth < 85 and connection.rectCenterWidth > 0):
                walking.turnLeft(config,0.5)
                now =0
                if connection.previous == connection.data_arr and now==1:
                    standing.stableStance(config)
                now +=1
                    
            while (connection.rectCenterWidth < 224 and connection.rectCenterWidth > 85):
                walking.strafeLeft(config,0.5)
                now =0
                if connection.previous == connection.data_arr and now==1:
                    standing.stableStance(config)
                now +=1

            while (connection.rectCenterWidth < 416 and connection.rectCenterWidth > 224):
                print ("random")#if personYLocationBorder
                now =0
                if connection.previous == connection.data_arr and now==1:
                    standing.stableStance(config)
                now +=1
                    
            while (connection.rectCenterWidth < 555 and connection.rectCenterWidth > 416):
                walking.strafeRight(config,0.5)
                now =0
                if connection.previous == connection.data_arr and now==1:
                    standing.stableStance(config)
                now +=1

            while (connection.rectCenterWidth < 640 and connection.rectCenterWidth > 10055):
                walking.turnRight(config,0.5)
                now =0
                if connection.previous == connection.data_arr and now==1:
                    standing.stableStance(config)
                now +=1

except KeyboardInterrupt:
    standing.sit(config)
    config.serialConn.close()
    connection.conn.close()