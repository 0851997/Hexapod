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
connection = server.Server('192.168.43.5',8787,ready)
mythread = threading.Thread(target=connection.connect)
mythread.start()
ready.wait()
thread = threading.Thread(target=connection.run)
thread.start()

try:
    if config.serialConn.isOpen():
        standing.stableStance(config, 0.2)
        #timeout = time.time() + 5
        # while(True):
        #     mode = input("Press a key for movement command: ")
        #     print(connection.rectCenterWidth)
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
        #             standing.stableStance(config, 0.2)
        #             #break
        #         elif mode == 'x':
        #             standing.sit(config)
        #             #break
                    
        #THIS IS THE INTERFACE FOR THE END OF THE PROJECT
        while(True):
            print('while true loop')
            #turnLeftBoudaries = 0 - 85
            #strafeLeftBoundary = 85 - 224
            #forwardBackwardBoundary = 224 - 416
            #strafeRightBoundary = 416 - 555
            #turnRightBoundary = 555 - 640
            #print(connection.rectCenterWidth)
            if (connection.rectCenterWidth < 85 and connection.rectCenterWidth > 0):
                standing.stableStance(config, 0.2)
                walking.turnLeft(config, 0.5)
                print('turnleft')
                # now =0
                # if connection.previous == connection.rectCenterWidth and now==1:
                #     standing.stableStance(config, 0.2)
                #     #break
                # now +=1
                # connection.previous=connection.rectCenterWidth
                    
            elif (connection.rectCenterWidth < 224 and connection.rectCenterWidth > 85):
                standing.stableStance(config, 0.2)
                walking.strafeLeft(config, 0.5)
                print('strafeleft')
                #now =0
                # if connection.previous == connection.rectCenterWidth and now==1:
                #     standing.stableStance(config, 0.2)
                #     #break
                # now +=1
                # connection.previous=connection.rectCenterWidth

            elif (connection.rectCenterWidth < 416 and connection.rectCenterWidth > 224):
                #front 85 - 220
                #stand 220 - 265
                #back 265 - 615
                print('mid')
                #connection.dimensionRectangleWidth
                if connection.dimensionRectangleWidth > 85 and connection.dimensionRectangleWidth < 220:
                    standing.stableStance(config, 0.2)
                    walking.tripodWalking(config, 0.5)
                    print('forward')
                elif connection.dimensionRectangleWidth > 220 and connection.dimensionRectangleWidth < 265:
                    standing.stableStance(config, 0.2)
                    print('stand')
                elif connection.dimensionRectangleWidth > 265 and connection.dimensionRectangleWidth < 615:
                    standing.stableStance(config, 0.2)
                    walking.reverse(config, 0.5)
                    print('reverse')
                #connection.previous=connection.rectCenterWidth
                # now =0
                # if connection.previous == connection.rectCenterWidth and now==1:
                #     standing.stableStance(config, 0.2)
                #     #break
                # now +=1
                # connection.previous=connection.rectCenterWidth
                    
            elif (connection.rectCenterWidth < 555 and connection.rectCenterWidth > 416):
                walking.strafeRight(config, 0.5)
                print('straferight')
                # now =0
                # if connection.previous == connection.rectCenterWidth and now==1:
                #     standing.stableStance(config, 0.2)
                #     #break
                # now +=1
                # connection.previous=connection.rectCenterWidth

            elif (connection.rectCenterWidth < 640 and connection.rectCenterWidth > 555):
                walking.turnRight(config, 0.5)
                print('turnright')
                # now =0
                # if connection.previous == connection.rectCenterWidth and now==1:
                #     standing.stableStance(config, 0.2)
                #     #break
                # now +=1
                # connection.previous=connection.rectCenterWidth

            elif connection.rectCenterWidth < 0 or connection.rectCenterWidth > 640:
                standing.stableStance(config, 0.2)
                print('standing pause')
                #break
            else:
                standing.stableStance(config, 0.2)
                print('else')
                #break
            time.sleep(0.5)

except KeyboardInterrupt:
    standing.sit(config)
    config.serialConn.close()
    connection.conn.close()